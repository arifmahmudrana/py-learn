from dataclasses import dataclass
import re


@dataclass
class Citizen:

    id: str
    name: str
    email: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative.")
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, self.email):
            raise ValueError("It's not an email address.")
        if len(self.name) > 20:
            raise ValueError("Name cannot exceed 20 characters.")


xiaoxu = Citizen("id1", "xiaoxu gao", "xiaoxu.gao@ing.com", 27)
xiaoxu = Citizen("id1", "xiaoxu1234567890123456789",
                 "highsmallxu@gmail.com", 27)
# ValueError: Name cannot exceed 20 characters.
xiaoxu = Citizen("id1", "xiaoxu gao", "highsmallxu@gmail.c", 27)
# ValueError: It's not an email address.
xiaoxu = Citizen("id1", "xiaoxu gao", "highsmallxu@gmail.com", -27)
# ValueError: Age cannot be negative.
