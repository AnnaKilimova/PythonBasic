# Створіть файл lib.py, помістіть в нього функції вашої гри.
# Імпортуйте гру в основний файл і запустіть гру з основного файлу

import random

word_choice = ('rock', 'paper', 'scissors')
user_choice = input('Su-e-fa!: ')
comp_choice = random.choice(word_choice)


def game(user: str, comp: 'value from tuple') -> str:
    """
    The function is intended for 'Rock paper scissors' game
    :param user:
    :param comp:
    :return: In this case you just need to display the result without using it further, so the function does not contain return
    """
    option_one = user_choice == 'paper' and comp_choice == 'rock'
    option_two = user_choice == 'rock' and comp_choice == 'scissors'
    option_three = user_choice == 'scissors' and comp_choice == 'paper'
    result = f'User: {user_choice} V/S Comp: {comp_choice}'
    if user_choice not in word_choice:
        print('You have definitely got the wrong game')
    elif option_one or option_two or option_three:
        print(f'{result} \nThe winner is USER')
    elif user_choice == comp_choice:
        print(f'{result} \nIt is a TIE')
    else:
        print(f'{result} \nThe winner is COMP')


if __name__ == '__main__':
    game(user_choice, comp_choice)
