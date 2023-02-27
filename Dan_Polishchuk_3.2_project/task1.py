import sqlite3
from sqlite3 import connect, OperationalError
from pandas import read_csv


class DB:
    def __init__(self, file_path, db_path):
        self.file_path = file_path
        self.db_path = db_path
        self.conn = connect(self.db_path)
        self.cur = self.conn.cursor()
        self.df = read_csv(self.file_path, index_col=0)

    @staticmethod
    def get_value_txt(item):
        info = item.strip().split(",")
        return info

    def type_definition(self):
        file_type = self.file_path.split(".")
        try:
            if file_type[-1] == "txt":
                self.insert_txt_data()
            elif file_type[-1] == "csv":
                self.insert_csv_data()
            else:
                print("Currently only .txt and .csv formats are supported, please choose on of them")
        except OperationalError:
            print('')

    def insert_csv_data(self):
        self.file_path = self.file_path.split("\\")
        table_name = self.file_path[-1].split(".")
        self.df.to_sql(table_name[0], self.conn, if_exists="replace", index=True)
        self.conn.commit()
        self.conn.close()

    def insert_txt_data(self):
        self.file_path = self.file_path.split("\\")
        table_name = self.file_path[-1].split(".")
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name[0]} (
                            Year,
                            Player,
                            Position,
                            Team,
                            Age,
                            Nationality
                            )""")
        with open(self.file_path) as f:
            file_data = f.readlines()
        for item in file_data:
            self.cur.execute("""INSERT INTO NBA_MVP_Awards_Last_10_Years(Year, Player, Position, Team, Age, Nationality)
                           VALUES(?, ?, ?, ?, ?, ?)""", (self.get_value_txt(item)[0], self.get_value_txt(item)[1],
                                                         self.get_value_txt(item)[2], self.get_value_txt(item)[3],
                                                         self.get_value_txt(item)[4], self.get_value_txt(item)[5]))
        self.conn.commit()
        self.conn.close()


txt_file = "C:\\Uni_tasks\\Dan_Polishchuk_3.2_project\\NBA_MVPs.txt"
csv_file = "C:\\Uni_tasks\\Dan_Polishchuk_3.2_project\\IMD_Top_100.csv"
txt_db = "C:\\Uni_tasks\\Dan_Polishchuk_3.2_project\\NBA_MVPs.db"
csv_db = "C:\\Uni_tasks\\Dan_Polishchuk_3.2_project\\IMD_Top_100.db"


if __name__ == "__main__":

    try:
        Digga = DB(txt_file, txt_db)
        Digga.insert_txt_data()
        Digga.type_definition()
 
    except ValueError as e:
        print(e)

    except TypeError as e:
        print(e)

    except IndexError as e:
        print(e)

    except sqlite3.OperationalError as e:
        print(e)

