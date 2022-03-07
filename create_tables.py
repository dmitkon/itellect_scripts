import pandas as pd
from os.path import exists

GAMES_TABLE = {'name': "Игры", 'data': {'Игра': ["ЧГК", "Пентагон"], 
                                        'Код': ['chgk', 'pg'], 
                                        'Вкл': [1, 0],
                                        'Коэфф': [1, 1],
                                        'Кол-во': [12, '-']}}
TEAMS_TABLE = {'name': "Команды", 'data': {'Название': [], 'Номер': []}}
PENTAGON_TABLE = {'name': "Пентагон", 'data': {'№ команды': [], 'Тема': [], 'Подсказка': [], 'Зачёт': []}}

def get_chgk_answers_table(quest_cnt):
    return {'name': "ЧГК", 'data': {'Вопрос ' + str(key + 1):[] for key in range(quest_cnt)}}

def create_table_kit(path, table):
    if not exists(path):
        sheet = pd.DataFrame(table.get('data'))
        
        writer = pd.ExcelWriter(path, engine='openpyxl')

        sheet.to_excel(writer, sheet_name=table.get('name'), index=False)
        
        for i, column in enumerate(sheet):
            column_width = max(sheet[column].astype(str).map(len).max(), len(column))
            writer.sheets[table.get('name')].column_dimensions[chr(i + 65)].width = column_width + 2

        writer.save()