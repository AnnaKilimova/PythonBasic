#  "[дата, на яку актуальний курс]"
# 1. [назва валюти 1] to UAH: [значення курсу валюти 1]

import requests
import pprint
import json

res = requests.request('GET', 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')

dirty_text = res.text.split('\n,')

possible = '",:'

my_list = []

for elements in range(1, len(dirty_text) - 1):
    correct_elements = ''
    for symbols in range(0, len(dirty_text[elements])):
        if dirty_text[elements][symbols].isalnum() or dirty_text[elements][symbols] in possible:
            correct_elements += dirty_text[elements][symbols]
    my_list.append(correct_elements.split(','))
# print(my_list)

squares = {}
my_count = -1
squares_in = {}

for k in my_list:
    # print(k[0])
    my_count += 1
    for a in range(0, len(my_list)):
        for i in k:
            # print(i)
            in_dict = i.split(':')
            squares_in[in_dict[0]] = in_dict[1]
            squares[my_count] = squares_in


print(f'squares = {squares}')
print(f'type(squares) = {type(squares)}')

for key, value in squares.items():
    print(key, '->', value)
    # print(f'type(key) = {type(key)}')
    # print(f'type(value) = {type(value)}')



# my_list = ['"r030":959,"txt":"Золото","rate":6967635,"cc":"XAU","exchangedate":"03072023"']
# new_list = my_list[0].split(',')
# print(f'len(my_list) = {len(my_list)}')
#
# squares = {}
# my_count = -1
# squares_in = {}

# for a in range(0, len(my_list)):
#     my_count += 1
#     for i in new_list:
#         in_dict = i.split(':')
#         squares_in[in_dict[0]] = in_dict[1]
#         squares[my_count] = squares_in
#
#
# print(f'squares = {squares}')
# print(f'type(squares) = {type(squares)}')
#
# for key, value in squares.items():
#     print(key, '->', value)
#     print(f'type(key) = {type(key)}')
#     print(f'type(value) = {type(value)}')



# for elements in range(1, len(dirty_text) - 1):
#     correct_elements = ''
#     for symbols in range(0, len(dirty_text[elements])):
#         if dirty_text[elements][symbols].isalnum() or dirty_text[elements][symbols] in possible:
#             correct_elements += dirty_text[elements][symbols]
#     my_list.append(correct_elements.split(','))
# print(my_list[0][0])
# print(type(my_list[0][0]))

#
# new_list = []
#
# for i in my_list:
#     new_list = i.split(',')
#     print(new_list)



# new_list = []
# my_set = set()
#
# for i in my_list:
#     new_list.append(i.split(','))
# print(new_list)

# for i in my_set:
#     my_set = set(i)
#     print(my_set)


# squares = {}
# my_count = -1
#
# for i in my_list:
#     my_count += 1
#     my_str = '{' + i + '}'
#     squares[my_count] = my_str
#
# for key, value in squares.items():
#     print(key, '->', value)
#     print(type(key))


# squares = {}
# my_count = -1
# for i in my_list:
#     my_count += 1
#     my_str = '{' + i + '}'
#     squares[my_count] = my_str
#
# for key, value in squares.items():
#     print(key, '->', value)
#     print(type(key))


    # key[value] = json.loads(value)



# print(squares)
# print(type(squares[0]))


# squares = {}
#
# squares[0] = 0
# squares[1] = 1
# squares[2] = 4
# squares[3] = 9
# squares[4] = 16
# squares[5] = 25






# my_str = '{' + my_list[0] + '}'
# my_dict = json.loads(my_str)
# keys = ['r030', 'cc']
#
# for key in keys:
#     my_dict.pop(key, None)
# print(my_dict)









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