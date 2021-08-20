import sqlite3


conn = sqlite3.connect(r'C:\Users\kszpo\PycharmProjects\nowa_biblioteka\nowa_biblioteka.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT not NULL,"
              "name TEXT not NULL, surname TEXT not NULL)")
    c.execute("CREATE TABLE IF NOT EXISTS  books (name TEXT not NULL, surname TEXT not NULL, title TEXT not NULL, "
              "status TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT not NULL)")
    c.execute("CREATE TABLE IF NOT EXISTS  hire_books (id_book INTEGER not NULL, id_student INTEGER not NULL, "
              "date_hire DATE, date_return DATE, id INTEGER PRIMARY KEY AUTOINCREMENT not NULL)")


create_table()
c.close()
conn.close()
