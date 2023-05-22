#Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

lst1 = ['1', '2', 3, True, False, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 0.25]
lst2 = []

for x in lst1:
    if type(x) == int or type(x) == float:
        lst2.append(x)
print(lst2)


# Варіант якщо дані типу bool чи числовы строки перетворити на числа

# for x in lst1:
#     if str(x).isdigit() or type(x) == bool:
#         lst2.append(int(x))
#     if type(x) == float:
#         lst2.append(x)
# print(lst2)
