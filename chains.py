import pandas as pd

class Chains:
    def __init__(self, teams):
        self.teams = teams
        self.results = []

    def read_chains(self, path):
        data = pd.read_excel(path)
        
        row = 0
        while row < data.shape[0]:
            len_list = str(data['Длины'][row]).split(' ')
            len_list = [int(len) for len in len_list]
            result = {'num': int(data['Номер'][row]), 'guessed_cnt': int(data['Кол-во угаданных'][row]), 'len': len_list}

            self.results.append(result)

            row += 1

#        if data.shape[0] < len(self.teams):
#            for i in range(len(self.teams) - data.shape[0]):
#                self.results.append({'num': 0, 'guessed_cnt': 0, 'len': []})

    def get_table(self):
        teams = []
        chains = []
        guessed_list = []
        results = []

        for result in self.results:
            teams.append(self.get_team(result.get('num')))
            guessed_list.append(result.get('guessed_cnt'))
            chains.append(sum(list(map(lambda x: x * x, result.get('len'))), start=0))
            results.append(guessed_list[-1] + chains[-1])

        table = pd.DataFrame({'Команда': teams, 'Цепочки': chains, 'Угадано': guessed_list, 'Итог': results})
        table = table.sort_values('Итог', ascending=False)

        return table

    def get_team(self, num):
        name = "name"
        for team in self.teams:
            if team.num == num:
                name = team.name
        
        return name
