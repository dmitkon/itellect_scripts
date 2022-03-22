import pandas as pd
from general.team import Team

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

def read_table(path):
    data = pd.read_excel(path)
    # data = data.sort_values('Номер')

    return data