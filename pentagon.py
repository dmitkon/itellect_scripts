import pandas as pd
import numpy as np

class Pentagon:
    def __init__(self, teams):
        self.teams = teams
        self.themes = []

    def read_pentagon(self, path):
        data = pd.read_excel(path)

        themes_cnt = data['Тема'].max()
        if str(themes_cnt) == str(np.nan):
            themes_cnt = 0

        self.themes = [[] for i in range(themes_cnt)]

        row = 0
        while row < data.shape[0]:
            if str(data['№ команды'][row]) != str(np.nan):
                self.themes[data['Тема'][row] - 1].append({'num': int(data['№ команды'][row]), 'hint': int(data['Подсказка'][row]), 'res': int(data['Зачёт'][row])})

            row += 1

    def get_table(self):
        names = [team.name for team in self.teams]
        tables = pd.DataFrame({'Команда': names})
        
        for i in range(len(self.themes)):
            table = pd.DataFrame()

            for j in range(5):
                title = 'П' + str(5 - j) + '.' + str(i + 1)
                table[title] = [np.nan for team in self.teams]

            for result in self.themes[i]:
                title = 'П' + str(result.get('hint')) + '.' + str(i + 1)
                table.loc[result.get('num') - 1, title] = result.get('res')

            title = 'Итог ' + str(i + 1)
            row = 0
            result = []
            while row < table.shape[0]:     
                result.append(get_theme_result(table, i, row))

                row += 1

            table[title] = result

            tables = tables.join(table)

        total = []
        row = 0
        while row < tables.shape[0]:
            sum = 0

            for i in range(len(self.themes)):
                title = 'Итог ' + str(i + 1)
                sum += tables[title][row]

            total.append(sum)

            row += 1

        tables['Итог'] = total

        return tables
    
def get_theme_result(table, i, row):
    result = 0
    hint = 5
    minus = 0

    while hint > 0:
        title = 'П' + str(hint) + '.' + str(i + 1)

        if table[title][row] == 1:
            result = hint

        if table[title][row] == 0:
            result = 0
            minus += 1

        hint -= 1

    return result - minus
