from chgk import Chgk
from chains import Chains
from pentagon import Pentagon
import pandas as pd
import create_tables as ct
import read_tables as rt

class Main:
    def run(self):
        print("Run app")

        ct.create_table_kit("Игры.xlsx", ct.GAMES_TABLE)
        ct.create_table_kit("Команды.xlsx", ct.TEAMS_TABLE)
        ct.create_table_kit("ЧГК_ответы.xlsx", ct.get_chgk_answers_table(12))
        ct.create_table_kit("Пентагон_ответы.xlsx", ct.PENTAGON_TABLE)

        games_set = rt.read_games("Игры.xlsx")
        teams = rt.read_teams("Команды.xlsx")

        if 'chgk' in games_set:
            chgk = Chgk(teams)
            chgk.read_quest("ЧГК_ответы.xlsx")

        # if 'pg' in games_set:
        #     pentagon = Pentagon(teams)
        #     pentagon.read_pentagon("Пентагон_ответы.xlsx")

        # chains = Chains(teams)
        # chains.read_chains("Цепочки_ответы.xlsx")
        
        # total_table = get_result(teams, chgk.get_table(), pentagon.get_table(), chains.get_table())
        # print(total_table)

        # write_table({'ЧГК': chgk.get_table(), 'Цепочки': chains.get_table(), 'Пентагон': pentagon.get_table(), 'Итог': total_table}, "./result/Протокол.xlsx")

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
