from random import randint

# Generate a random number between 1-10
random_number = randint(1, 10)
while True:
    # Ask user input
    user_input = None
    try:
        user_input = int(input('Guess a number between 1 and 10: '))
    except ValueError:
        print(f'Invalid user input {user_input}')
        continue
    except EOFError:
        print('\nThanks for playing. Bye!')
        break
    
    if user_input < random_number:
        print('Too low, try again!')
    elif user_input > random_number:
        print('Too high, try again!')
    else:
        print('You guessed it! You won!')
        play_again = input('Do you want to keep playing? (y/n) ')
        if play_again.lower() == 'n':
            print('Thanks for playing. Bye!')
            break
        random_number = randint(1, 10)
