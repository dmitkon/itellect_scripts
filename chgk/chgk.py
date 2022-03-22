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
        table = pd.DataFrame({'Команда': [team.name for team in self.teams], 'Номер': [team.num for team in self.teams]})
        
        quest_titles = []
        quest_rating = []
        for quest in self.quest:
            title = 'Вопрос ' + str(quest.get('num'))
            quest_titles.append(title)
            answers = []

            for team in self.teams:
                if team.num in quest.get('teams'):
                    answers.append(1)
                else:
                    answers.append(0)

            zero_cnt = 0
            for res in answers:
                if res == 0:
                    zero_cnt += 1
        
            quest_rating.append(zero_cnt/len(self.teams))

            table[title] = answers

        table['Итог'] = table[quest_titles].sum(axis=1)

        ratings = []

        for row in range(table.shape[0]):
            rating = 0
            
            for i, title in enumerate(quest_titles):
                if table[title][row] == 1:
                    rating += quest_rating[i]

            ratings.append(rating)

        table['Рейтинг'] = ratings

        return table
