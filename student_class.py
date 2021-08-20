class Student:
    def __init__(self, name, surname, username, id = 0):
        self.name = name
        self.surname = surname
        self.username = username
        self.id = id

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Username: {self.username}, ID: {self.id}"

    def __repr__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Username: {self.username}, ID: {self.id}"


