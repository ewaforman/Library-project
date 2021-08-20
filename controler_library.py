from flask import Flask, request
import json
from Repo_library import connect_to_db, RepositoryHire, RepositoryBooks, RepositoryStudent
from hire_class import Hire
from book_class import Book
from student_class import Student
from converter_class import Converter

app = Flask(__name__)

@app.route('/add_student', methods=['POST'])
def add_student():
    content = request.get_json()
    repository_student = RepositoryStudent()
    converter = Converter()
    student = converter.convert_student_to_obj(content)
    add_student_answer = repository_student.add_student(student)
    return add_student_answer

@app.route('/delete_student', methods=['DELETE'])
def delete_student():
    content = request.get_json()
    repository_student = RepositoryStudent()
    converter = Converter()
    id = converter.get_student_id(content)
    repository_student.delete_student(id)
    return f"Usunięto studenta o nr {id}."

@app.route('/update_student', methods=['POST'])
def update_student():
    content = request.get_json()
    repository_student = RepositoryStudent()
    converter = Converter()
    student = converter.convert_student_to_obj(content)
    repository_student.update_student(student)
    return content

@app.route('/select_student_by_username', methods=['GET'])
def select_student_by_username():
    content = request.get_json()
    repository_student = RepositoryStudent()
    student = repository_student.select_student_by_username(content["username"])
    student_json = json.dumps(student.__dict__)
    return student_json

@app.route('/get_all_students', methods=['GET'])
def get_all_student():
    repository_student = RepositoryStudent()
    student_list = repository_student.get_all_student()
    converter = Converter()
    json_string = json.dumps(student_list, default=converter.obj_dict)
    return json_string

@app.route('/count_all_students', methods=['GET'])
def count_all_student():
    repository_student = RepositoryStudent()
    number_of_students = repository_student.count_all_students()
    number_of_students = str(number_of_students)
    return f"Liczba studentów w bazie to: {number_of_students}."

@app.route('/add_book', methods=['POST'])
def add_book():
    content = request.get_json()
    repository_book = RepositoryBooks()
    converter = Converter()
    book = converter.convert_book_to_obj(content)
    repository_book.add_book(book)
    return "Dodano nową książkę."


@app.route('/delete_book', methods=['DELETE'])
def delete_book():
    content = request.get_json()
    repository_book = RepositoryBooks()
    converter = Converter()
    id = converter.get_book_id(content)
    repository_book.delete_book(id)
    return f"Usunięto książkę o nr {id}."

@app.route('/update_book', methods=['POST'])
def update_book():
    content = request.get_json()
    repository_book = RepositoryBooks()
    converter = Converter()
    book = converter.convert_book_to_obj_by_id(content)
    repository_book.update_book(book)
    return content

@app.route('/select_book_by_status', methods=['GET'])
def select_book_by_status():
    content = request.get_json()
    repository_book = RepositoryBooks()
    book_list_status = repository_book.select_book_by_status(content["status"])
    converter = Converter()
    books_json_list = json.dumps(book_list_status, default=converter.obj_dict)
    return books_json_list

@app.route('/get_all_books', methods=['GET'])
def get_all_books():
    repository_book = RepositoryBooks()
    book_list_status = repository_book.get_all_books()
    converter = Converter()
    books_json_list = json.dumps(book_list_status, default=converter.obj_dict)
    return books_json_list

@app.route('/count_all_books', methods=['GET'])
def count_all_books():
    repository_book = RepositoryBooks()
    number_of_books = repository_book.count_all_books()
    number_of_books = str(number_of_books)
    return f"Liczba ksiazek w bazie to: {number_of_books}."

@app.route('/add_hire', methods=['POST'])
def add_hire():
    content = request.get_json()
    repository_hire = RepositoryHire()
    converter = Converter()
    hire = converter.convert_hire_to_obj(content)
    hire_info = repository_hire.add_hire(hire)
    return hire_info

@app.route('/return_hire', methods=['POST'])
def return_hire():
    content = request.get_json()
    repository_hire_return = RepositoryHire()
    converter = Converter()
    hire = converter.convert_return_book_to_obj(content)
    return_info = repository_hire_return.return_book(hire)
    return return_info

@app.route('/get_full_info_hire', methods=['GET'])
def get_full_info_hire():
    content = request.get_json()
    repository_hire = RepositoryHire()
    converter = Converter()
    hire_obj = converter.convert_full_hire(content)
    hire_full_info_list = repository_hire.get_full_info_hire(hire_obj)
    hire_full_info_json = json.dumps(hire_full_info_list, default=converter.obj_dict)
    return hire_full_info_json


if __name__ == '__main__':
    app.run()