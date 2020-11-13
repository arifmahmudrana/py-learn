class Player:
    # class object attribute
    membership = True

    # dunder methods init/constructor
    def __init__(self, name, age):
        print(self.membership)
        print(Player.membership)
        self.name = name
        self.age = age
        # private property by convension
        self._type = 'player'

    def run(self, hello):
        print('run')
        print(f'print {self.name} {hello}')
        return 'done'

    @classmethod
    # can access class variable original class
    def get_instance(cls, name, age):
        return cls(name, age)

    @staticmethod
    # doesn't has access of cls
    def add_numbers(num1, num2):
        return num1 + num2


class Vehicle(Player):
    def run(self):
        print(Player.run(self, 'asdasdas'))
        print(super().run('asdasdasdas'))
        return 'Vehicle'

# Inheritance from Vehicle, Player


# class Wizard(Vehicle, Player):
class Wizard(Vehicle):
    pass


player1 = Player('Rana', 38)
player1.attack = 50


print(player1.name)
print(player1.age)
print(player1.attack)
print(player1.run('kidding me'))

wiz = Wizard('asdas', 12121)
print(wiz.run())
print(isinstance(wiz, Player))
print(isinstance(wiz, Vehicle))
print(dir(wiz))


class SuperList(list):
    def __len__(self):
        return 1000


super_list = SuperList([1, 2, 3])
print(super_list)
print(len(super_list))
super_list.append(2)
print(super_list)
print(len(super_list))
