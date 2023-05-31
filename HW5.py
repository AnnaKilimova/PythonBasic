# Доопрацюйте гру з заняття наступним чином:
#
# Додайте вибір слова з будь-якого джерела на ваш вибір
# Додайте лічильник спроб вгадати слово і вихід з цтклу по переповненню лічильника
# Додайте більш інформативні повідомлення (список можливих букв для введення, повідомлення про невірне введення,
# повідомлення про кількість спроб що залишилися і тд)
# Опційно. Додайте можливість повторювати гру. Запитати в гравця чи хоче він повторити гру Yes/No і повторювати
# якщо він введе Yes, завершити якщо введе No

choice_words = ('adventurous', 'clumsy', 'moody', 'stubborn', 'vulnerable', 'wise')

import random

available_letters = 'abcdefghijklmnopqrstyuwxvz'

while True:
    word = random.choice(choice_words)

    guessed_letters = []

    entered_letters = set()

    guess_result = '?' * len(word)

    for attempts_quantity in range(len(word)+3):

        print(f'guess_result = {guess_result}')

        user_letter = input('Enter the letter: ').lower()

        if user_letter in entered_letters or user_letter in guessed_letters:
            print('Duplicate!')
            print(f'guess_result = {guess_result}')
            print(f'You have {(len(word) + 3) - (attempts_quantity + 1)} more attempts')
        elif user_letter in word:
            guessed_letters.append(user_letter)
            guess_result = ''.join(['?' if char not in guessed_letters else char for char in word])
            print('Congratulations! You guessed the letter!!!')
            print(f'guess_result = {guess_result}')
            print(f'You have {(len(word) + 3) - (attempts_quantity + 1)} more attempts')
        elif len(user_letter) != 1:
            print('Too long or too short!')
            print(f'guess_result = {guess_result}')
            print(f'You have {(len(word) + 3) - (attempts_quantity + 1)} more attempts')
        elif user_letter not in available_letters:
            print('Unavailable!')
            print(f'guess_result = {guess_result}')
            print(f'You have {(len(word) + 3) - (attempts_quantity + 1)} more attempts')
        elif word.find(user_letter) == -1:
            print('This word does not contain that letter')
            print(f'guess_result = {guess_result}')
            print(f'You have {(len(word)+3) - (attempts_quantity + 1)} more attempts')

        entered_letters.add(user_letter)

        if guess_result == word:
            print('You are a winner!!!')
            break

    Question_Answer = input('Do you want to try again??? Enter Yes / No: ').lower()
    if Question_Answer == 'yes':
        continue
    else:
        print('Game over')
        break


print('The End')