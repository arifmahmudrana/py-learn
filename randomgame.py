from random import randint
from sys import argv

# pylint: disable=unbalanced-tuple-unpacking
# start, end = argv[1:3]
start, end = int(argv[1]), int(argv[2])

item = randint(start, end)

while int(input(f'Guess number between({start}, {end})?\n')) != item:
    print('Boo Boo wrong!!!')

print(f'===>>>Great job 😎️😎️😎️')
