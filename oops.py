class Player:
    # class object attribute
    membership = True

    # dunder methods init/constructor
    def __init__(self, name, age):
        print(self.membership)
        print(Player.membership)
        self.name = name
        self.age = age

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


player1 = Player('Rana', 38)
player1.attack = 50


print(player1.name)
print(player1.age)
print(player1.attack)
print(player1.run('kidding me'))
