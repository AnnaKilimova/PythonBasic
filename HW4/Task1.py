# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.

string_example = 'My cat and doog clearly like the piig'

words = string_example.split()

vowels = 'aeiouy'

new_words = []

for i in words:
    for j in i:
        if j in vowels:
            if i.find(j) + 1 > (len(i) - 1):
                break
            if i[i.find(j) + 1] in vowels and i.find(j) + 1 < (len(i) - 1):
                new_words.append(i)
                break
print(new_words)






# Kept it to myself!!!

# for i in words:
#     for j in i:
#         if j in vowels:
#             print(f'i = {i}')
#             print(f'j = {j}')
#             print(j in vowels)
#             # print(i[i.find(j) + 1])
#             print(len(i) - 1)
#             if i.find(j) + 1 > (len(i) - 1):
#                 break
#             if i[i.find(j) + 1] in vowels and i.find(j) + 1 < (len(i) - 1):
#                 print(i[i.find(j) + 1])
#                 new_words.append(i)
#                 print(new_words)
#                 break
