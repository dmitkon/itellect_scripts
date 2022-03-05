import pandas as pd
from team import Team

def read_games(path):
    data = pd.read_excel(path)

    row = 0
    games = set()
    while row < data.shape[0]:
        if data['Вкл'][row] == 1:
            games.add(data['Код'][row])
        
        row += 1

    return games

def read_teams(path):
    data = pd.read_excel(path)
    data = data.sort_values('Номер')

    row = 0
    teams = []
    while row < data.shape[0]:
        team = Team(data['Название'][row], int(data['Номер'][row]))
        teams.append(team)
        
        row += 1

    return teams