# Напишіть декоратор, який вимірює час виконання функції
# Задекоруйте цим декоратором вашу гру з попереднього домашнього завдання


import random
import time


def my_decorator(func):
    def function_wrapper(*args, **kwargs):
        start = time.monotonic()
        print(f'Start = {start}')
        result = func(*args, **kwargs)
        end = time.monotonic()
        print(f'End = {end}')
        print(f"Time taken is {end - start}s")
        return result

    return function_wrapper


word_choice = ('rock', 'paper', 'scissors')
user_choice = input('Su-e-fa!: ')
comp_choice = random.choice(word_choice)


@my_decorator
def game(user, comp):
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


game(user_choice, comp_choice)
