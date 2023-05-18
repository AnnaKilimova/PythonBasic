# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне :

# Попросіть користувача ввести свій вік (можно використати константу або input()).

# P.S. На екран має бути виведено лише одне повідомлення, якщо вік користувача містить цифру тільки відповідне
# повідомлення! Також подумайте над варіантами, коли введені невірні або неадекватні (неможливі) дані.

age = int(input('Введить свій вік'))
result = str(age).find('7')

if age < 6 and result == -1: #- якщо користувачу менше 6 - вивести повідомлення "Де твої батьки?"
    print('Де твої батьки?')
elif age < 16 and result == -1: # - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
    print('Це фільм для дорослих!')
elif age > 65 and result == -1: # - якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
    print('Покажіть пенсійне посвідчення!')
elif result != -1: # - якщо вік користувача містить цифру 7 - вивести повідомлення "Вам пощастить!"
    print('Вам пощастить!')
else: # - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
    print('А білетів вже немає!')
