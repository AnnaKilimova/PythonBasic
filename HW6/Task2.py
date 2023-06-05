# Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# у будь-якому іншому випадку повернути кортеж з цих аргументів

def dif_action(arg1, arg2):
    a = None
    if (type(arg1) is int or type(arg1) is float) and (type(arg2) is int or type(arg2) is float):
        return arg1 * arg2
    elif type(arg1) is str and type(arg2) is str:
        return arg1 + arg2
    else:
        return (arg1, arg2)

print(dif_action(3, 3))
print(dif_action('Hello ', 'world'))
print(dif_action(3, 'world'))