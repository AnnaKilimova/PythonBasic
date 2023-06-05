# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.
def conv_float(arg1):
    try:
        return float(arg1)
    except ValueError:
        return 0

print(conv_float('10'))
print(conv_float('ex'))
print(conv_float('10.2'))
print(conv_float(False))