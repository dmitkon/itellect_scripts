from chgk import Chgk
from chains import Chains
from pentagon import Pentagon
from team import Team
import pandas as pd

class Main:
    def run(self):
        print("Run app")

        teams = read_teams("Команды.xlsx")

        chgk = Chgk(teams)
        chgk.read_quest("ЧГК_ответы.xlsx")

        chains = Chains(teams)
        chains.read_chains("Цепочки_ответы.xlsx")

        pentagon = Pentagon(teams)
        pentagon.read_pentagon("Пентагон_ответы.xlsx")
        
        total_table = get_result(teams, chgk.get_table(), pentagon.get_table(), chains.get_table())
        print(total_table)

        write_table({'ЧГК': chgk.get_table(), 'Цепочки': chains.get_table(), 'Пентагон': pentagon.get_table(), 'Итог': total_table}, "./result/Протокол.xlsx")

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

def write_table(sheets, path):
    writer = pd.ExcelWriter(path, engine='openpyxl')

    for sheet_name in sheets.keys():
        sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()

def get_result(teams, chgk, pentagon, chains):
    teams = [team.name for team in teams]
    table = pd.DataFrame({'Команда': teams, 'ЧГК': [0 for i in range(chgk.shape[0])], 'Пентагон': [0 for i in range(pentagon.shape[0])], 'Цепочки': [0 for i in range(chgk.shape[0])]})

    row = 0
    while row < chgk.shape[0]:
        table.loc[get_index(table, 'Команда', chgk['Команда'][row]), 'ЧГК'] = chgk['Итог'][row]
        
        row += 1

    row = 0
    while row < pentagon.shape[0]:
        table.loc[get_index(table, 'Команда', pentagon['Команда'][row]), 'Пентагон'] = pentagon['Итог'][row]
        
        row += 1
    
    row = 0
    while row < chains.shape[0]:
        table.loc[get_index(table, 'Команда', chains['Команда'][row]), 'Цепочки'] = chains['Итог'][row]
        
        row += 1

    row = 0
    total = []
    while row < chains.shape[0]:
        total.append(table['ЧГК'][row]*2 + table['Пентагон'][row]*0.5 + table['Цепочки'][row]*0.1)
        
        row += 1

    table['Итог'] = total

    table = table.sort_values('Итог', ascending=False)

    return table

def get_index(table, title, value):
    row = 0
    index = 0

    while row < table.shape[0]:
        if table[title][row] == value:
            index = row
        
        row += 1

    return index
