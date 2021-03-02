import string
import random


chars = [random.choice(string.ascii_uppercase) for _ in range(
    3)] + [random.choice(string.ascii_lowercase) for _ in range(3)] + [random.choice(string.digits) for _ in range(3)] + [random.choice(string.punctuation) for _ in range(3)]

random.shuffle(chars)
print(''.join(chars))
