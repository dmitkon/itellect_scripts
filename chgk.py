import pandas as pd

class Chgk:
    def __init__(self, teams):
        self.teams = teams
        self.quest = []

    def read_quest(self, path):
        data = pd.read_excel(path)

        quest_cnt = data.shape[1]

        for i in range(quest_cnt):
            self.quest.append({'num': i + 1, 'teams': set(data['Вопрос ' + str(i + 1)])})

    def get_table(self):
        teams_name = [team.name for team in self.teams]
        table = pd.DataFrame({'Команда': teams_name})
        
        quest_titles = []
        for quest in self.quest:
            title = 'Вопрос ' + str(quest.get('num'))
            quest_titles.append(title)
            answers = []

            for team in self.teams:
                if team.num in quest.get('teams'):
                    answers.append(1)
                else:
                    answers.append(0)
        
            table[title] = answers

        table['Итог'] = table[quest_titles].sum(axis=1)

        return table
