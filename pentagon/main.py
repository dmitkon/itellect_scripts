from pentagon.pentagon import Pentagon
import general.create_tables as ct
import general.read_tables as rt
import general.write_tables as wt

class Main:
    def run(self):
        print("Run app")
        
        print("Создать игру - 1, Получить результаты - любой символ:")
        task = input()
        
        if task == "1":
            ct.create_table_kit("Пентагон_ответы.xlsx", ct.PENTAGON_TABLE)
        else:
            print("Название:")
            name = input()

            teams = rt.read_teams("Команды.xlsx")
            pentagon = Pentagon(teams)
            pentagon.read_pentagon("Пентагон_ответы.xlsx")

            wt.write_table({name: pentagon.get_table()}, "./result/" + name + ".xlsx")
