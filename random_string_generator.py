from random import choice, randint, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from typing import List


def validate_charset(charset: List[str]) -> None:
    """Validates charset raises ValueError if invalid data."""

    if not isinstance(charset, list):
        raise ValueError('charset must be a list')

    if len(charset) < 4:
        raise ValueError('charset must contain at least 4 items')

    for char in charset:
        if not isinstance(char, str):
            raise ValueError('charset must be a list of string')

        if not len(char):
            raise ValueError('charset items can not be empty')


def validate_length(length: int) -> None:
    """Validates length raises ValueError if length less then 4."""

    if length < 4:
        raise ValueError('length must be equal or greater then zero')


def random_string_list(length: int, charset: List[str] = [ascii_uppercase, ascii_lowercase, punctuation, digits]) -> List[str]:
    """Generate random list string of length from charset and returns list."""

    validate_length(length)
    validate_charset(charset)

    random_list_of_string = []
    for i, char in enumerate(charset):
        random_list_of_string.extend([choice(char) for _ in range(
            randint(1, length - len(random_list_of_string) - 3 + i))])

    return random_list_of_string


def random_string(length: int, charset: List[str] = [ascii_uppercase, ascii_lowercase, punctuation, digits]) -> str:
    """Generate random string of length and returns the string."""

    validate_length(length)
    validate_charset(charset)
    shuffle(charset)
    chars = random_string_list(length, charset)
    shuffle(chars)

    return ''.join(chars)


if __name__ == '__main__':
    from sys import argv

    length = int(argv[-1]) if len(argv) > 1 else 12
    print(random_string(length), end='')
    # print(random_string(length, charset=[
    #       ascii_uppercase, ascii_uppercase, ascii_lowercase, ascii_lowercase]), end='')
