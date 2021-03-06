import sqlite3

from werkzeug.exceptions import NotFound

from student_class import Student
from book_class import Book
from hire_class import Hire
import json


def connect_to_db():
    conn = sqlite3.connect(r'C:\Users\kszpo\PycharmProjects\nowa_biblioteka\nowa_biblioteka.db')
    c = conn.cursor()
    return c, conn


class RepositoryStudent:
    def add_student(self, student):
        c, conn = connect_to_db()
        c.execute(f"SELECT name, surname, username, id FROM students WHERE surname = '{student.surname}'")
        myresult = c.fetchall()
        username = ''
        for krotka in myresult:
            name, surname, username, id = krotka

        if username == f"{student.username}":
            add_student_refusal = "Taki student jest juz w bazie."
            return add_student_refusal
        else:
            c, conn = connect_to_db()
            c.execute(f"INSERT INTO students (name, surname, username) VALUES ('{student.name}', '{student.surname}',"
                      f" '{student.username}')")
            add_student_accept = "Dodałeś nowego studenta."
            conn.commit()
            return add_student_accept

    def delete_student(self, id_student):
        c, conn = connect_to_db()
        c.execute(f"SELECT id FROM students")
        myresult = c.fetchall()
        id_list = []
        for krotka in myresult:
            id = krotka
            id_list.append(id[0])
        id_student_int = int(id_student)
        if id_student_int in id_list:
            c.execute(f"DELETE FROM students WHERE id = '{id_student_int}'")
            conn.commit()
            delete_student_answer = "Usunięto studenta."
            return delete_student_answer
        else:
            delete_student_answer = "Nie ma takiego studenta w bazie."
            return delete_student_answer

    def update_student(self, student):
        c, conn = connect_to_db()
        c.execute(f"UPDATE students SET name = '{student.name}', surname = '{student.surname}'"
                  f"WHERE username = '{student.username}'")
        conn.commit()

    def select_student_by_username(self, username):
        c, conn = connect_to_db()
        c.execute(f"SELECT * FROM students WHERE username = '{username}'")
        myresult = c.fetchall()
        try:
            id, name, surname, username = myresult[0]
            student = Student(name, surname, username, id)
            conn.commit()
            return student
        except IndexError:
            raise NotFound(IndexError)

    def get_all_student(self):
        c, conn = connect_to_db()
        c.execute(f"SELECT * FROM students")
        myresult = c.fetchall()

        all_student_list = []

        for krotka in myresult:
            id, name, surname, username = krotka
            student = Student(name, surname, username, id)
            all_student_list.append(student)
        return all_student_list

    def count_all_students(self):
        c, conn = connect_to_db()
        c.execute("SELECT count(id) FROM students")

        myresult = c.fetchall()
        number_all_students = myresult[0][0]
        return number_all_students


class RepositoryBooks:
    def isValidated(self, book_list):
        for element in book_list:
            if element == "":
                return False
        return True

    def add_book(self, book):
        c, conn = connect_to_db()
        list_of_books = [f'{book.name}', f'{book.surname}', f'{book.title}']

        validated = self.isValidated(list_of_books)

        if validated:
            c.execute(f"INSERT INTO books (name, surname, title, status) VALUES ('{book.name}', '{book.surname}',"
                      f" '{book.title}', '{book.status}')")
            conn.commit()
            add_book_answer = "Dodano nową książkę."
            return add_book_answer
        else:
            add_book_answer = "Wypełnij wszystkie pola."
            return add_book_answer

    def delete_book(self, id_book):
        c, conn = connect_to_db()
        c.execute(f"SELECT id FROM books")
        myresult = c.fetchall()
        id_list = []
        for krotka in myresult:
            id = krotka
            id_list.append(id[0])
        id_book_int = int(id_book)
        if id_book_int in id_list:
            c.execute(f"DELETE FROM books WHERE id = '{id_book_int}'")
            conn.commit()
            delete_book_answer = "Usunięto książkę."
            return delete_book_answer
        else:
            delete_book_answer = "Nie ma takiej książki w bazie."
            return delete_book_answer

    def update_book(self, book):
        c, conn = connect_to_db()
        c.execute(f"UPDATE books SET name = '{book.name}', surname = '{book.surname}', title = "
                  f"'{book.title}', status = '{book.status}' WHERE id = '{book.id}'")
        conn.commit()

    def select_book_by_status(self, status):
        c, conn = connect_to_db()
        c.execute(f"SELECT * FROM books WHERE status = '{status}'")
        myresult = c.fetchall()

        # name_columns = c.execute('SELECT name FROM pragma_table_info("books") ORDER BY cid')
        # name_columns_all = []
        #
        # for name_column in name_columns:
        #     name_column = "".join(name_column)
        #     name_columns_all.append(name_column)
        # print(name_columns_all)

        book_list_status = []

        for krotka in myresult:
            name, surname, title, status, id = krotka
            book = Book(name, surname, title, status, id)
            book_list_status.append(book)
        return book_list_status

    def select_book_by_id(self, id):
        c, conn = connect_to_db()
        c.execute(f"SELECT * FROM books WHERE id = '{id}'")
        myresult = c.fetchall()

        try:
            name, surname, title, status, id = myresult[0]
            book = Book(name, surname, title, status, id)
            conn.commit()
            return book
        except IndexError:
            raise NotFound(IndexError)

    def get_all_books(self):
        c, conn = connect_to_db()
        c.execute(f"SELECT * FROM books")
        myresult = c.fetchall()

        all_books_list = []

        for krotka in myresult:
            name, surname, title, status, id = krotka
            book = Book(name, surname, title, status, id)
            all_books_list.append(book)
        return all_books_list

    def count_all_books(self):
        c, conn = connect_to_db()
        c.execute("SELECT count(id) FROM books")

        myresult = c.fetchall()
        number_all_books = myresult[0][0]
        return number_all_books


class RepositoryHire:
    def add_hire(self, hire):
        c, conn = connect_to_db()
        c.execute(f"SELECT hire_books.id_book, books.status FROM hire_books LEFT JOIN books ON "
                  f"hire_books.id_book = books.id  "
                  f"WHERE id_book = '{hire.id_book}'")
        myresult = c.fetchall()
        status = ""
        for krotka in myresult:
            id_book, status = krotka

        if status == 'hired':
            hire_info_refusal = "Ta książka jest już wypożyczona."
            return hire_info_refusal
        else:
            c, conn = connect_to_db()
            c.execute(f"INSERT INTO hire_books (id_book, id_student, date_hire) VALUES ('{hire.id_book}', "
                      f"'{hire.id_student}','{hire.date_hire}')")
            conn.commit()
            c, conn = connect_to_db()
            c.execute(f"UPDATE books SET status = 'hired' WHERE id = '{hire.id_book}'")
            conn.commit()
            hire_info_accept = "Wypożyczyłeś książkę."
            return hire_info_accept

    def return_book(self, hire):
        c, conn = connect_to_db()
        c.execute(f"UPDATE hire_books SET date_return = '{hire.date_return}' WHERE id_book = '{hire.id_book}'")
        conn.commit()

        c, conn = connect_to_db()
        c.execute(f"UPDATE books SET status = 'available' WHERE id = '{hire.id_book}'")
        conn.commit()
        answer = "Ksiazka zostala oddana."
        return answer


    def get_full_info_hire(self, hire):
        c, conn = connect_to_db()
        c.execute(f"SELECT hire_books.id_book, hire_books.id_student, students.name, "
                  f"students.surname, books.name, books.surname, books.title, hire_books.date_hire, "
                  f"hire_books.date_return, hire_books.id FROM hire_books LEFT JOIN students ON hire_books.id_student "
                  f"= students.id LEFT JOIN books ON hire_books.id_book = books.id  "
                  f"WHERE id_book = '{hire.id_book}' and id_student='{hire.id_student}'")
        myresult = c.fetchall()
        full_info_hire_all = []
        for krotka in myresult:
            id_book, id_student, student_name, student_surname, author_name, author_surname, title, date_hire, \
            date_return, id = krotka
            full_hire = Hire(id_book, id_student, date_hire, date_return, id, student_name, student_surname,
                             author_name, author_surname, title)
            full_info_hire_all.append(full_hire)
        conn.commit()
        return full_info_hire_all

    def get_all_hires(self):
        c, conn = connect_to_db()
        c.execute(f"SELECT hire_books.id_book, hire_books.id_student, students.name, "
                  f"students.surname, books.name, books.surname, books.title, hire_books.date_hire, "
                  f"hire_books.date_return, hire_books.id FROM hire_books LEFT JOIN students ON hire_books.id_student "
                  f"= students.id LEFT JOIN books ON hire_books.id_book = books.id  ")

        myresult = c.fetchall()
        full_info_hire_all = []
        for krotka in myresult:
            id_book, id_student, student_name, student_surname, author_name, author_surname, title, date_hire, \
            date_return, id = krotka
            full_hire = Hire(id_book, id_student, date_hire, date_return, id, student_name, student_surname,
                             author_name, author_surname, title)
            full_info_hire_all.append(full_hire)
        conn.commit()
        return full_info_hire_all



