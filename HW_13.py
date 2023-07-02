#  "[дата, на яку актуальний курс]"
# 1. [назва валюти 1] to UAH: [значення курсу валюти 1]

import requests
import pprint
import json

res = requests.request('GET', 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')

dirty_text = res.text.split('\n,')
print(len(dirty_text))

possible = '",:'

my_list = []

for elements in range(1, len(dirty_text) - 1):
    correct_elements = ''
    for symbols in range(0, len(dirty_text[elements])):
        if dirty_text[elements][symbols].isalnum() or dirty_text[elements][symbols] in possible:
            correct_elements += dirty_text[elements][symbols]
    my_list.append(correct_elements)
print(my_list)

# for i in my_list:
#     print(i)


# a = res.text
# b = a.split('\n,')
# print(len(b))
#
# possible = '",:'
#
# my_list = []
#
# for i in range(1, len(b) - 1):
#     new_b = ''
#     for j in range(0, len(b[i])):
#         if b[i][j].isalnum() or b[i][j] in possible:
#             new_b += b[i][j]
#     my_list.append(new_b)
# print(my_list)