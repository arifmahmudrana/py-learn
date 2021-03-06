import re


class Name:
    def __get__(self, obj):
        return self.value

    def __set__(self, obj, value):
        if len(value) > 20:
            raise ValueError("Name cannot exceed 20 characters.")
        self.value = value


class Email:
    def __get__(self, obj):
        return self.value

    def __set__(self, obj, value):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, value):
            raise ValueError("It's not an email address.")
        self.value = value


class Age:
    def __get__(self, obj):
        return self.value

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self.value = value


class Citizen:

    name = Name()
    email = Email()
    age = Age()

    def __init__(self, id, name, email, age):
        self.id = id
        self.name = name
        self.email = email
        self.age = age


class Salary:
    def __get__(self, obj):
        self.value

    def __set__(self, obj, value):
        if value < 1000:
            raise ValueError("Salary cannot be lower than 1000.")
        self.value = value


class Employee:
    name = Name()
    email = Email()
    age = Age()
    salary = Salary()

    def __init__(self, id, name, email, age, salary):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.salary = salary


xiaoxu = Employee("id1", "xiaoxu gao", "xiaoxugao@gmail.com", 27, 1000)
xiaoxu = Employee("id1", "xiaoxu gao", "xiaoxugao@gmail.com", 27, 999)
# ValueError: Salary cannot be lower than 1000.


xiaoxu = Citizen("id1", "xiaoxu gao", "xiaoxugao@gmail.com", 27)
xiaoxu = Citizen("id1", "xiaoxu1234567890123456789",
                 "highsmallxu@gmail.com", 27)
# ValueError: Name cannot exceed 20 characters.
xiaoxu = Citizen("id1", "xiaoxu gao", "highsmallxu@gmail.c", 27)
# ValueError: It's not an email address.
xiaoxu = Citizen("id1", "xiaoxu gao", "highsmallxu@gmail.com", -27)
# ValueError: Age cannot be negative.
