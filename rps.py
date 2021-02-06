from random import randrange

options = ['Rock', 'Paper', 'Scissor']


def user_input():
    '''
    Loops until user selects a valid input
    exits from program if user inputs q

    :return: user selection
    :rtype: int | str
    '''
    while True:
        user_selection = input('''Please select any one from below Press q for quit
1. Rock
2. Paper
3. Scissor
>> ''')
        if user_selection.lower() == 'q':
            return 'q'
        try:
            user_input = int(user_selection)
            if user_input < 1 or user_input > 3:
                raise ValueError(f'Invalid input {user_input}')

            return user_input
        except ValueError:
            print(f'Invalid user input {user_selection} select from 1-3')


def is_winner(first, second):
    '''
    checks the winner between first and second
    :return: if winner first
    :rtype: bool
    '''
    return (first is 1 and second is 3) or (first is 2 and second is 1) or (first is 3 and second is 2)


def find_winner(user_selection, computer_selection):
    '''
    Determines the winner  from user input and computer input
    if user wins returns 1 if drawn returns 0 if computer wins returns -1

    :param user_selection int: user selection from prompt
    :param computer_selection int: computer selection

    :return: the winner
    :rtype: int
    :raises ValueError: if None condition matches
    '''
    if user_selection is computer_selection:
        return 0
    elif is_winner(user_selection, computer_selection):
        return 1
    elif is_winner(computer_selection, user_selection):
        return -1

    raise ValueError(f'Invalid state {user_selection} {computer_selection}')


def run():
    '''
    Runs the program and finds the winner
    '''
    user_won = 0
    computer_won = 0
    while True:
        computer_selection = randrange(3) + 1
        user_selection = None
        add_extra = ''
        try:
            user_selection = user_input()
        except EOFError:
            user_selection = 'q'
            add_extra = '\n'

        if user_selection == 'q':
            print_result(user_won, computer_won, add_extra)
            break

        try:
            winner = find_winner(user_selection, computer_selection)

            if winner is 0:
                print(
                    f'Match drawn no body wins 😓️ you choose {options[user_selection - 1]} and computer choose {options[computer_selection - 1]}')
            elif winner is 1:
                print(
                    f'Woow you won 😎️ you choose {options[user_selection - 1]} and computer choose {options[computer_selection - 1]}')
                user_won += 1
            elif winner is -1:
                print(
                    f'Hard luck you loose ☹️  you choose {options[user_selection - 1]} and computer choose {options[computer_selection - 1]}')
                computer_won += 1

        except ValueError:
            print(
                f'Unpredictable result {user_selection} {computer_selection}')
            print_result(user_won, computer_won)
            break


def print_result(user, computer, add_extra=''):
    print(f'{add_extra}User won {user} and computer won {computer}')


if __name__ == '__main__':
    run()
