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
        games = rt.read_games("Игры.xlsx")
        
        ct.create_table_kit("Команды.xlsx", ct.TEAMS_TABLE)
        ct.create_table_kit("ЧГК_ответы.xlsx", ct.get_chgk_answers_table(games.get_game_options('chgk').get('Кол-во')))
        ct.create_table_kit("Пентагон_ответы.xlsx", ct.PENTAGON_TABLE)

        teams = rt.read_teams("Команды.xlsx")
        result_tables = {}

        if 'chgk' in games.codes_set:
            chgk = Chgk(teams)
            chgk.read_quest("ЧГК_ответы.xlsx")
            result_tables[games.get_game_options('chgk').get('Игра')] = chgk.get_table()

        if 'pg' in games.codes_set:
            pentagon = Pentagon(teams)
            pentagon.read_pentagon("Пентагон_ответы.xlsx")
            result_tables[games.get_game_options('pg').get('Игра')] = pentagon.get_table()

        # chains = Chains(teams)
        # chains.read_chains("Цепочки_ответы.xlsx")
        
        total_table = get_result(games, teams, result_tables)
        print(total_table)

        # write_table(total_table, result_tables, "./result/Протокол.xlsx")

def get_result(games, teams, tables):
    result = pd.DataFrame({'Команда': [team.name for team in teams]})

    for key in tables:
        table = tables.get(key)
        result[key] = table['Итог']

    total = []
    for row in range(result.shape[0]):
        sum = 0
        
        for code in games.data['Код']:
            if code in games.codes_set:
                sum += result[games.get_game_options(code).get('Игра')][row]*games.get_game_options(code).get('Коэфф')
        
        total.append(sum)

    result['Итог'] = total

    result = result.sort_values('Итог', ascending=False)

    return result
