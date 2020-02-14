import psycopg2
from pprint import pprint


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='postgres',user='postgres',host='localhost',password='postgres',port='5432'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("cannot connect to database")

    def create_table(self):
        create_table_command = "CREATE TABLE pet(id serial PRIMARY KEY,name varchar(100),age integer NOT NULL)"
        self.cursor.execute(create_table_command)

    def insert_new_record(self):
        new_record=("misa meo5","9")
        insert_command="INSERT INTO pet(name,age) VALUES('"+new_record[0]+"','"+new_record[1] + "')"
        pprint(insert_command)
        self.cursor.execute(insert_command)

    def query_all(self):
        self.cursor.execute("SELECT * FROM pet")
        cats=self.cursor.fetchall()
        for cat in cats:
            pprint("each pet:{0}".format(cat))

    def update_record(self):
        update_command="UPDATE pet SET age=10 where id=1"
        self.cursor.execute(update_command)

    def drop_table(self):
        drop_command="DROP TABLE pet"
        self.cursor.execute(drop_command)
if __name__ == '__main__':
    database_connection = DatabaseConnection()
    database_connection.create_table()
    database_connection.insert_new_record(
    database_connection.query_all()
    database_connection.update_record()
    database_connection.drop_table()


