# Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові.
# Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'".
# Слово та номер символу отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".

word = input('Type a word: ')
symbol = input(f'Type a symbol number from 0 to {len(word)-1}: ')
if symbol.isdigit():
    symbol = int(symbol)
    if int(symbol) > len(word)-1:
        print('Try again! The value exceeds the permissible value')
    else:
        print(f'The {symbol} symbol in {word} is {word[symbol]}')
else:
    print('Try again! You can type only a number!!!')



