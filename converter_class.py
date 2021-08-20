from student_class import Student
from book_class import Book
from hire_class import Hire
from Repo_library import connect_to_db


class Converter:
    def convert_student_to_obj(self, content):
        name = content['name']
        surname = content['surname']
        username = content['username']
        student = Student(name, surname, username)
        return student

    def get_student_id(self, content):
        id = content['id']
        return id

    def obj_dict(self, obj):
        return obj.__dict__

    def convert_book_to_obj(self, content):
        name = content['name']
        surname = content['surname']
        title = content['title']
        book = Book(name, surname, title)
        return book

    def get_book_id(self, content):
        id = content['id']
        return id

    def convert_book_to_obj_by_id(self, content):
        name = content['name']
        surname = content['surname']
        title = content['title']
        status = content['status']
        id = content['id']
        book = Book(name, surname, title, status, id)
        return book

    def convert_hire_to_obj(self, content):
        id_book = content['id_book']
        id_student = content['id_student']
        date_hire = content['date_hire']
        hire = Hire(id_book, id_student, date_hire)
        return hire

    def convert_return_book_to_obj(self, content):
        id_book = content['id_book']
        date_return = content['date_return']
        hire = Hire(id_book)
        hire.set_date_of_return(date_return)
        # hire_return.date_return = date_return
        return hire

    def convert_full_hire(self, content):
        id_book = content['id_book']
        id_student = content['id_student']
        hire = Hire(id_book, id_student)
        return hire




