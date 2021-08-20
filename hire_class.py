class Hire:
    def __init__(self, id_book, id_student = None, date_hire = None, date_return=None, id=0, student_name= None,
                 student_surname=None, author_name = None, author_surname = None, title = None):
        self.id = id
        self.id_book = id_book
        self.id_student = id_student
        self.student_name = student_name
        self.student_surname = student_surname
        self.author_name = author_name
        self.author_surname = author_surname
        self.title = title
        self.date_hire = date_hire
        self.date_return = date_return


    def set_date_of_return(self, date_of_return):
        self.date_return = date_of_return

    def __str__(self):
        return f"ID book: {self.id_book}, ID student: {self.id_student}, Hire ID: {self.id}, Student name: " \
               f"{self.student_name}, Student surname: " \
               f"{self.student_surname}, Author name: {self.author_name}, Author surname: {self.author_surname}, " \
               f"Tytuł książki: {self.title}, date of hire: {self.date_hire}, date of return: {self.date_return}"

    def __repr__(self):
        return f"ID book: {self.id_book}, ID student: {self.id_student}, ID: {self.id}, Student name: " \
               f"{self.student_name}, Student surname: " \
               f"{self.student_surname}, Author name: {self.author_name}, Author surname: {self.author_surname}, " \
               f"Tytuł książki: {self.title}, date of hire: {self.date_hire}, date of return: {self.date_return}"


# obiekt_Hire = Hire(1, 1)
# print(obiekt_Hire)