class Book:
    def __init__(self, name, surname, title, status="available", id=0):
        self.id = id
        self.name = name
        self.surname = surname
        self.title = title
        self.status = status

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Title: {self.title}, Status: {self.status}, ID: {self.id}"

    def __repr__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Title: {self.title}, Status: {self.status}, ID: {self.id}"


# obiekt1 = Book("ff", "gg", "ee")
# print(obiekt1)