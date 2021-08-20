class HireBook:
    def __init__(self, id, id_book, id_student, date_hire, date_return):
        self.id = id
        self.id_book = id_book
        self.id_student = id_student
        self.date_hire = date_hire
        self.date_return = date_return

    def __str__(self):
        return f"ID: {self.id}, ID_book: {self.id_book}, ID_student: {self.id_student}, Date_hire: {self.date_hire}, " \
               f"Date_return: {self.date_return}"

    def __repr__(self):
        return f"ID: {self.id}, ID_book: {self.id_book}, ID_student: {self.id_student}, Date_hire: {self.date_hire}, " \
               f"Date_return: {self.date_return}"