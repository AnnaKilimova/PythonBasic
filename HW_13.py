# Подключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ), отримайте теперішній курс валют и запишіть його в TXT-файл в такому форматі:
#  "[дата, на яку актуальний курс]"
# 1. [назва валюти 1] to UAH: [значення курсу валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу валюти 3]
# ...
# n. [назва валюти n] to UAH: [значення курсу валюти n]
#
# опціонально передбачте для користувача можливість обирати дату, на яку він хоче отримати курс
#
# P.S.  За можливості зробіть все за допомогою ООП

import datetime
import requests
from datetime import date


a = input('Day __: ')
b = input('Month __: ')
c = input('Year 20__: ')

try:
    my_date = date(day=int(a), month=int(b), year=int(c))
except (TypeError, AttributeError, ValueError):
    my_date = 'Try again'
    print(my_date)


class CreationList:
    def __init__(self, x, my_list1, my_list2, my_list3):
        self.res_x = requests.request('GET', x)
        self.txt_list = my_list1
        self.rate_list = my_list2
        self.exchangedate_list = my_list3

        new_data = self.res_x.json()

        count = 0

        for i in new_data:
            for key, value in new_data[count].items():
                if key == 'txt':
                    my_list1.append(value)
                elif key == 'rate':
                    my_list2.append(value)
                elif key == 'exchangedate':
                    try:
                        if type(my_date) is datetime.date and str(my_date.year)[:2] == '20' and len(str(my_date.year)) == 4:
                            my_list3.append(my_date)
                        else:
                            my_list3.append(value)
                    except AttributeError:
                        print('Incorrect year')

            count += 1

    def __str__(self):
        return f'Lists: {self.res_x} {self.txt_list} {self.rate_list}'


class CreationDoc:
    def __init__(self, my_list0, my_list1, my_list2, my_list3):
        self.my_list = my_list0
        self.res_x = my_list1
        self.txt_list = my_list2
        self.rate_list = my_list3

        for k in range(0, len(my_list1)):
            my_str = f'{my_list1[k]}\n {k+1}. [{my_list2[k]}] to UAH: [{my_list3[k]}]\n'
            my_list0.append(my_str)

    def __str__(self):
        return f'my_list = {self.my_list}'


creation_list = CreationList('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json', [], [], [])

creation_doc = CreationDoc([], creation_list.exchangedate_list, creation_list.txt_list, creation_list.rate_list)

print(creation_doc)

with open('my.txt_new', 'w') as file:
    for h in creation_doc.my_list:
        file.write(h)
