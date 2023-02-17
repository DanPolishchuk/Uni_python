import sqlite3
from sqlite3 import connect
from prettytable import from_db_cursor
from voice import DBMS_speak


class DBMS:

    def __init__(self):
        self.conn = connect("C:\\Uni_tasks\\Dan_Polishchuk_3.3_project\\Лаб_3.4.db")
        self.cur = self.conn.cursor()

    def main(self):

        print("\n1. Create a data table\n2. Viewing and editing the data table\n3. Reporting\n4. Exit")
        choice = int(input("Type here: "))

        if choice == 1:
            self.create()
        elif choice == 2:
            self.edit_table()                                         # chooses an option
        elif choice == 3:
            self.reporting()
        elif choice == 4:
            DBMS_speak("It was a pleasure doing business with you, take care of yourself")
            exit()
        else:
            self.error()

    def wellcome_back(self, something):
        if something == "digga":
            self.main_menu()

    def main_menu(self):
        DBMS_speak("Okay, I got you, welcome back to the main menu")
        self.main()

    def error(self):
        DBMS_speak("Seems like something went wrong, start again from the beginning")
        self.main()

    def show_table(self, table_name):
        self.cur.execute(f"""SELECT * FROM {table_name}""")                # prints entire table
        table = from_db_cursor(self.cur)
        print(table)

    def create(self):
        DBMS_speak("\nGreat, let`s do it, but be aware, if you want to return to the main menu, write 'digga'\n")
        DBMS_speak("Okay, firstly give a name to the new data table")
        table_name = input('Type here: ')
        self.wellcome_back(table_name)
        DBMS_speak('How many columns would you like to create?')
        column_count = input("Type here: ")
        self.wellcome_back(column_count)

        column_names = []
        name_type = []
        for i in range(int(column_count)):
            names = input(f"Name the column {i+1}: ")
            self.wellcome_back(names)
            types = input(f"Column type {i+1}: ")                            # sets up a table
            self.wellcome_back(types)
            column_names.append(names)
            name_type.append(names+" "+types.upper())

        try:
            self.cur.execute(f"""CREATE table {table_name} ({name_type[0]})""")
            for i in range(1, int(column_count)):
                self.cur.execute(f"""ALTER TABLE {table_name} ADD {name_type[i]}""")       # creates a table

        except sqlite3.OperationalError:
            try:
                DBMS_speak(f"Table {table_name} already exists, provide another name")
                new_name = input("Type new name here: ")
                self.cur.execute(f"""CREATE table {new_name} ({name_type[0]})""")
                for i in range(1, int(column_count)):
                    self.cur.execute(f"""ALTER TABLE {new_name} ADD {name_type[i]}""")
            except sqlite3.OperationalError:
                self.error()
        self.conn.commit()

        self.show_table(table_name)
        DBMS_speak("Let`s fill out the table, type one to confirm or two to return back")
        action = int(input("\n1 - confirm\n2 - return to the main menu\nType here: "))
        table_info = self.cur.execute(f"""SELECT * FROM {table_name}""")
        columns = [description[0] for description in table_info.description]
        if action == 1:
            self.add_values(table_name, columns)
        elif action == 2:
            self.main_menu()
        else:
            self.error()

    def table_choice(self):
        DBMS_speak("\nAlright, now i will show you all available tables, and you should choose one")
        self.cur.execute("""SELECT name FROM sqlite_master WHERE type="table" """)
        tables = self.cur.fetchall()
        print("\nData tables: ")                                                    # shows all tables
        for i in range(len(tables)):
            print(f"{i+1}.", tables[i][0])

    def edit_table(self):
        self.table_choice()

        table_name = input("Submit a name here: ")
        self.wellcome_back(table_name)                                             # picks the table
        self.show_table(table_name)

        table_info = self.cur.execute(f"""SELECT * FROM {table_name}""")       # getting universal 1st column of any
        columns = [description[0] for description in table_info.description]                               # table

        DBMS_speak("\nOkay, now please pick one of the options below:")
        action = input("\n1. Edit rows\n2. Remove rows\n3. Add data to rows\n4. Return to the main menu\nType here: ")
        self.wellcome_back(action)

        if int(action) == 1:
            self.edit_rows(table_name, columns)
        elif int(action) == 2:
            self.remove_rows(table_name, columns)
        elif int(action) == 3:
            self.add_values(table_name, columns)
        elif int(action) == 4:
            self.main_menu()
        else:
            self.error()

    def edit_rows(self, table_name, columns):
        row = input("\nValue(that is located in first column) of the row that you want to edit: ")
        self.wellcome_back(row)
        column_name = input("Name of column that you want to edit: ")
        self.wellcome_back(column_name)                                              # table editing
        new_value = input("\nPlease provide new value:\n - ")
        self.wellcome_back(new_value)
        self.cur.execute(f"""UPDATE {table_name} SET "{column_name}"="{new_value}" 
                             WHERE "{columns[0]}"="{row}" """)
        self.conn.commit()
        self.show_table(table_name)
        DBMS_speak("Changes are executed, would you like to repeat the whole process?")
        answer = input("Yes/no: ")
        if answer == "yes" or answer == "Yes" or answer == "YES":
            self.edit_rows(table_name, columns)
        elif answer == "no" or answer == "NO" or answer == "No":
            self.main_menu()
        else:
            self.error()

    def remove_rows(self, table_name, columns):
        DBMS_speak('Now provide value(that is located in first column) of the row,'
                   'that you want to remove from the table')
        row = input("Type here: ")                                                         # rows removing
        self.wellcome_back(row)
        self.cur.execute(f"""DELETE FROM {table_name} WHERE {columns[0]}="{row}"; """)
        self.conn.commit()
        self.show_table(table_name)
        DBMS_speak("Removing is completed, would you like to repeat the whole process?")
        answer = input("Yes/no: ")
        if answer == "yes" or answer == "Yes" or answer == "YES":
            self.remove_rows(table_name, columns)
        elif answer == "no" or answer == "NO" or answer == "No":
            self.main_menu()
        else:
            self.error()

    def add_values(self, table_name, columns):
        DBMS_speak("Great, now please add new value to every column of the data table")
        values = []
        columns_list = []
        for i in range(len(columns)):
            value = input(f"{columns[i]}: ")
            values.append(value)
            columns_list.append(columns[i])
        self.cur.execute(f"""INSERT INTO {table_name}("{columns[0]}") VALUES("{values[0]}") """)
        for i in range(1, len(columns)):
            self.cur.execute(f"""UPDATE {table_name} SET "{columns[i]}"="{values[i]}"
                                 WHERE "{columns[0]}"="{values[0]}" """)
        self.conn.commit()
        self.show_table(table_name)                                               # adds new values to data table
        DBMS_speak("Awesome, all new values are already added to data table, "
                   "would you like to repeat the whole process?")
        answer = input("Yes/no: ")
        if answer == "yes" or answer == "Yes" or answer == "YES":
            self.add_values(table_name, columns)
        elif answer == "no" or answer == "NO" or answer == "No":
            self.main_menu()
        else:
            self.error()

    def reporting(self):
        DBMS_speak("Now are only two reports available, you should pick one")
        report = int(input("\n1. Information about customer with id = 10\n2. Cities where available balance > 3000"
                           "\nType here: "))
        report_name = ""
        if report == 1:
            report_name = "Report1"
            self.cur.execute(f""" CREATE TABLE IF NOT EXISTS {report_name} AS SELECT 
                                  ADDRESS, CITY, CUST_TYPE_CD, FED_ID, POSTAL_CODE, STATE, ACCOUNT_ID, AVAIL_BALANCE, 
                                  CLOSE_DATE, LAST_ACTIVITY_DATE, OPEN_DATE, PENDING_BALANCE, STATUS, OPEN_BRANCH_ID, 
                                  OPEN_EMP_ID, PRODUCT_CD, OFFICER_ID, FIRST_NAME, LAST_NAME, START_DATE, TITLE
                                  FROM CUSTOMER
                                  INNER JOIN ACCOUNT ON CUSTOMER.CUST_ID = ACCOUNT.CUST_ID
                                  INNER JOIN OFFICER ON ACCOUNT.CUST_ID = OFFICER.CUST_ID
                                  LIMIT 1""")
            self.conn.commit()
            self.show_table(report_name)
        elif report == 2:
            report_name = "Report2"
            self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {report_name} AS SELECT AVAIL_BALANCE, CITY
                                 FROM ACCOUNT
                                 INNER JOIN CUSTOMER ON ACCOUNT.CUST_ID = CUSTOMER.CUST_ID
                                 WHERE AVAIL_BALANCE > 3000""")
            self.conn.commit()
            self.show_table(report_name)

        else:
            self.error()

        DBMS_speak("Would you like to sort or filter this report?")
        answer = input("Yes/no: ")
        if answer == "yes" or answer == "Yes" or answer == "YES":
            self.filter_sort(report_name)
        elif answer == "no" or answer == "NO" or answer == "No":
            self.main_menu()
        else:
            self.error()

    def filter_sort(self, table_name):
        DBMS_speak("Now, please choose option")
        option = int(input("\n1. Ascending sort\n2. Descending sort\n3. Filter < > =\nType here: "))
        if option == 1:
            column = input("\nProvide a name of column: ")
            sorted_table = self.cur.execute(f""" SELECT * FROM {table_name} ORDER BY "{column}" ASC """)
            table = from_db_cursor(sorted_table)
            print(table)
            self.main()

        elif option == 2:
            column = input("\nProvide a name of column: ")
            sorted_table = self.cur.execute(f""" SELECT * FROM {table_name} ORDER BY "{column}" DESC """)
            table = from_db_cursor(sorted_table)
            print(table)
            self.main()

        elif option == 3:
            column = input("\nProvide a name of column: ")
            filter_symbol = input("Choose a symbol(> < =): ")
            number = input("Enter a number to filter: ")
            filtered_table = self.cur.execute(f""" SELECT * FROM {table_name} 
                                                   WHERE "{column}" {filter_symbol} {number} """)
            table = from_db_cursor(filtered_table)
            print(table)
            self.main()

        else:
            self.error()


if __name__ == "__main__":
    try:
        dbms = DBMS()
        DBMS_speak("\nHi, how could I assist you today? Choose one of the options below")
        dbms.main()

    except ValueError as e:
        print(e)

    except IndexError as e:
        print(e)

    except sqlite3.OperationalError as e:
        print(e)

    except TypeError as e:
        print(e)
