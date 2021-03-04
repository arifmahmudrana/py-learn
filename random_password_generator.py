
from random import choice, randint, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from sys import argv

pass_length = int(argv[-1]) if len(argv) > 1 else 12

charset = [ascii_uppercase, ascii_lowercase, punctuation, digits]

shuffle(charset)

first = [choice(charset[0]) for _ in range(randint(1, pass_length - 3))]

second = [choice(charset[1])
          for _ in range(randint(1, pass_length - len(first) - 2))]

third = [choice(charset[2]) for _ in range(
    randint(1, pass_length - len(first) - len(second) - 1))]

fourth = [choice(charset[3]) for _ in range(
    randint(1, pass_length - len(first) - len(second) - len(third)))]

chars = first + second + third + fourth

shuffle(chars)
print(''.join(chars), end='')
