# Задача_1: Створіть дві змінні first=10, second=30.
# Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.

first = 10
second = 30

print(first + second)
print(second - first)
print(first * second)
print(second / first)
print(second ** first)
print(second // first)
print(second % first)

# Задача_2: Створіть змінну і почергово запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння

result = None
result = first < second
print(result)
result = first > second
print(result)
result = first == second
print(result)
result = first != second
print(result)

# Задача: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world".
# Виведіть на екран
str1 = 'Hello '
str2 = 'world'
concatenation = str1 + str2
print(concatenation)
