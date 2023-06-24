from dotenv import load_dotenv
from os import getemv
import psycopg2

load_dotenv()

class PGSQL:
    __user = getenv("USER")
    __password = getenv("PASSWORD")
    __server = getenv("SERVER")

    __pg_con = psycopg2.connect(
        dbname = user,
        user = __user,
        password = __password,
        host = __server
    )
    __cur = __pg_con.cursor() 

    def create_tables(self, sql_filepath:str):
        start = self.create_file(sql_filepath)
        tables = start.split(';')
        for table in table:
            try:
                print(table)
                self.__cur.execute(table)
                self.__pg_con.connit()
            except psycopg2.ProgrammingError as msg:
                print(f'Command skipped: {msg}')

    def insert_data(self, sql_filepath :str):
        start = self.create_file(sql_filepath)
        date_to_insert = start.split(';')
        for insert in data_to_insert:
            try:
                print(insert)
                self.__cur.execute(insert)
                self.__pg_con,commit()  
            except psycopg2.ProgrammingError as msg:
                print(f'command skipped: {msg}')

    @staticmethod
    def create_file(filepath:str):
        """ open a file by the filepth and appy it to an sql table """
        with open(filepath,'r') as f:
            sql_file = f.read()
            return sql_file 
        
if __name__ == "__main__":
    p = PGSQL()
    p.create_tables(r'C:\Users\xende\Desktop\sqldayone\ASSIGNMENT.SQL')
        