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
    name = request.form['name']
    surname = request.form['surname']
    username = request.form['username']
    content = {'name': name, 'surname': surname, 'username': username}
    request1 = request
    print(request)
    # print(content)

    # content = request.get_json()
    # print(type(content))
    # print(content)
    repository_student = RepositoryStudent()
    converter = Converter()
    student = converter.convert_student_to_obj(content)
    add_student_answer = repository_student.add_student(student)
    answer_dict = {'message': add_student_answer}
    print(answer_dict)
    # answer_json = json.dumps(answer_dict)
    # print(type(answer_json))
    return answer_dict

@app.route('/delete_student', methods=['DELETE'])
def delete_student():
    # content = request.get_json()
    id = request.form['id']
    content = {'id': id}
    repository_student = RepositoryStudent()
    converter = Converter()
    id = converter.get_student_id(content)
    repository_student.delete_student(id)
    delete_answer = f"Usunięto studenta o id {id}."
    delete_answer_dict = {"message": delete_answer}
    return delete_answer_dict

@app.route('/update_student', methods=['POST'])
def update_student():
    content = request.get_json()
    repository_student = RepositoryStudent()
    converter = Converter()
    student = converter.convert_student_to_obj(content)
    repository_student.update_student(student)
    return content

@app.route('/select_student_by_username', methods=['POST'])
def select_student_by_username():
    # content = request.get_json()
    username = request.form['username']
    content = {'username': username}
    repository_student = RepositoryStudent()
    student = repository_student.select_student_by_username(content["username"])
    student_json = json.dumps(student.__dict__)
    print("dupa")
    print(student_json)
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
    number_of_students_dict = {"number": number_of_students}
    print(number_of_students_dict)
    return number_of_students_dict

@app.route('/add_book', methods=['POST'])
def add_book():
    # content = request.get_json()
    name = request.form['name']
    surname = request.form['surname']
    title = request.form['title']
    content = {'name': name, 'surname': surname, 'title': title}
    repository_book = RepositoryBooks()
    converter = Converter()
    book = converter.convert_book_to_obj(content)
    repository_book.add_book(book)
    answer_dict = {"message": "Dodano nową książkę."}
    return answer_dict


@app.route('/delete_book', methods=['DELETE'])
def delete_book():
    # content = request.get_json()
    id = request.form['id']
    content = {'id': id}
    repository_book = RepositoryBooks()
    converter = Converter()
    id = converter.get_book_id(content)
    repository_book.delete_book(id)
    delete_answer = f"Usunięto książkę o id {id}."
    delete_answer_dict = {"message": delete_answer}
    return delete_answer_dict


@app.route('/update_book', methods=['POST'])
def update_book():
    name = request.form['name']
    surname = request.form['surname']
    title = request.form['title']
    content = {'name': name, 'surname': surname, 'title': title}
    # content = request.get_json()
    repository_book = RepositoryBooks()
    converter = Converter()
    book = converter.convert_book_to_obj_by_id(content)
    repository_book.update_book(book)
    return content

@app.route('/select_book_by_status', methods=['POST'])
def select_book_by_status():
    # content = request.get_json()
    print("dupa")
    status = request.form['status']
    content = {'status': status}
    repository_book = RepositoryBooks()
    book_list_status = repository_book.select_book_by_status(content["status"])
    converter = Converter()
    books_json_list = json.dumps(book_list_status, default=converter.obj_dict)
    print(books_json_list)
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
    number_of_books_dict = {"number": number_of_books}
    return number_of_books_dict

@app.route('/add_hire', methods=['POST'])
def add_hire():
    # content = request.get_json()
    id_book = request.form['id_book']
    id_student = request.form['id_student']
    date_hire = request.form['date_hire']
    content = {'id_book': id_book, 'id_student': id_student, 'date_hire': date_hire}
    repository_hire = RepositoryHire()
    converter = Converter()
    hire = converter.convert_hire_to_obj(content)
    hire_info = repository_hire.add_hire(hire)
    hire_info_json = {"message": hire_info}
    print(hire_info_json)
    return hire_info_json

@app.route('/return_hire', methods=['POST'])
def return_hire():
    # content = request.get_json()
    id_book = request.form['id_book']
    date_return = request.form['date_return']
    content = {'id_book': id_book, 'date_return': date_return}
    repository_hire_return = RepositoryHire()
    converter = Converter()
    hire = converter.convert_return_book_to_obj(content)
    return_info = repository_hire_return.return_book(hire)
    return_info_json = {"message": return_info}
    return return_info_json

@app.route('/get_full_info_hire', methods=['GET'])
def get_full_info_hire():
    content = request.get_json()
    repository_hire = RepositoryHire()
    converter = Converter()
    hire_obj = converter.convert_full_hire(content)
    hire_full_info_list = repository_hire.get_full_info_hire(hire_obj)
    hire_full_info_json = json.dumps(hire_full_info_list, default=converter.obj_dict)
    return hire_full_info_json

@app.route('/get_all_hires', methods=['GET'])
def get_all_hires():
    # content = request.get_json()
    # repository_hire = RepositoryHire()
    # converter = Converter()
    # hire_obj = converter.convert_full_hire(content)
    # hire_full_info_list = repository_hire.get_all_hires()
    # hire_full_info_json = json.dumps(hire_full_info_list, default=converter.obj_dict)
    # return hire_full_info_json

    repository_hire = RepositoryHire()
    hire_list = repository_hire.get_all_hires()
    converter = Converter()
    hire_json_list = json.dumps(hire_list, default=converter.obj_dict)
    print(hire_json_list)
    return hire_json_list


if __name__ == '__main__':
    app.run()