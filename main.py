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
        result_tables = {}

        if 'chgk' in games_set:
            chgk = Chgk(teams)
            chgk.read_quest("ЧГК_ответы.xlsx")
            result_tables['ЧГК'] = chgk.get_table()

        if 'pg' in games_set:
            pentagon = Pentagon(teams)
            pentagon.read_pentagon("Пентагон_ответы.xlsx")
            result_tables['Пентагон'] = pentagon.get_table()

        # chains = Chains(teams)
        # chains.read_chains("Цепочки_ответы.xlsx")
        
        total_table = get_result(teams, result_tables)
        print(total_table)

        # write_table(total_table, result_tables, "./result/Протокол.xlsx")

def get_result(teams, tables):
    result = pd.DataFrame({'Команда': [team.name for team in teams]})

    for key in tables:
        table = tables.get(key)
        result[key] = table['Итог']

    row = 0
    total = []
    for row in range(result.shape[0]):
        total.append(result['ЧГК'][row]*2)
        
        row += 1

    result['Итог'] = total

    result = result.sort_values('Итог', ascending=False)

    return result
