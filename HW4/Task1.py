# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.

string_example = 'My cat and doog clEarly like the piig'

words = string_example.lower().split()

vowels = 'aeiouy'

new_words = []

for word in words:
    for letter in word:
        if letter in vowels:
            if word.find(letter) + 1 > (len(word) - 1):
                break
            if word[word.find(letter) + 1] in vowels and word.find(letter) + 1 < (len(word) - 1):
                new_words.append(word)
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
