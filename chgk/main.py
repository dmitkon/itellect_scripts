from chgk.chgk import Chgk
import general.create_tables as ct
import general.read_tables as rt
import general.write_tables as wt

class Main:
    def run(self):
        print("Run app")
        
        print("Создать игру - 1, Получить результаты - любой символ:")
        task = input()
        
        if task == "1":
            print("Кол-во вопросов:")
            quest_cnt = input()

            if quest_cnt.isdigit():
                ct.create_table_kit("ЧГК_ответы.xlsx", ct.get_chgk_answers_table(int(quest_cnt)))
            else:
                print("Ошибка ввода: введено не число")
        else:
            print("Название:")
            name = input()

            teams = rt.read_teams("Команды.xlsx")
            chgk = Chgk(teams)
            chgk.read_quest("ЧГК_ответы.xlsx")

            wt.write_table({name: chgk.get_table()}, "./result/" + name + ".xlsx")
