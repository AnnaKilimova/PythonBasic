# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

a = 'Ex-am-ple - 1, word , is a cats\''
b = a.split(' ')
c = []
for x in b:
    if x.isalpha() or x.isdigit() or len(x) > 1:
        c.append(x)
    else:
        continue
print(c) # printed words - removed dashes and symbols that are not words and are separate
print(f'Number of words per line is {len(c)}')







