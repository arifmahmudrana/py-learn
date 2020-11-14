def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            iterator*5
            next(iterator)
        except StopIteration:
            break


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # this line allows us to use the current number as the starting point for the iteration
        MyGen.current = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


# gen = MyGen(1, 100)
# for i in gen:
#     print(i)


class Fibonacci():
    current = 0
    first_item = 0
    second_item = 1

    def __init__(self, last):
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if Fibonacci.current == 0:
            Fibonacci.current += 1
            return 0
        elif Fibonacci.current == 1:
            Fibonacci.current += 1
            return 1
        elif Fibonacci.current <= self.last:
            total = Fibonacci.first_item + Fibonacci.second_item
            Fibonacci.first_item = Fibonacci.second_item
            Fibonacci.second_item = total
            Fibonacci.current += 1

            return total

        raise StopIteration


# gen = Fibonacci(20)
# for i in gen:
#     print(i)


def fib(number):
    a = 0
    b = 1
    for _ in range(number + 1):
        yield a
        temp = a
        a = b
        b += temp


for i in fib(20):
    print(i)
