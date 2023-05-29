# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166,
# "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною
# і максимальною ціною. Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"

lower_limit = 35.9
upper_limit = 37.339

# Option_1. For float values only

shop_dict = {'cito': 47.999, 'BB_studio': 42.999, 'momo': 49.999, 'main-service': 37.245, 'buy.now': 38.324,
             'x-store': 37.166, 'the_partner': 38.988, 'store': 37.720, 'rozetka': 38.003}

for key in shop_dict:
    if shop_dict[key] > lower_limit and shop_dict[key] < upper_limit:
            print(key)



# added a str element ('test': 'test') and used try for this option

# shop_dict = {'cito': 47.999, 'BB_studio': 42.999, 'momo': 49.999, 'main-service': 37.245, 'buy.now': 38.324,
#              'x-store': 37.166, 'the_partner': 38.988, 'store': 37.720, 'rozetka': 38.003, 'test': 'test'}
#
# for key in shop_dict:
#     try:
#         if shop_dict[key] > lower_limit and shop_dict[key] < upper_limit:
#             print(key)
#     except TypeError:
#             print('print_TypeError')
#     except Exception:
#             print('about all errors except KeyBoardInterrupt')
    # else:
    #     print('good')
    # finally:
    #     print('end')
    # When we add these blocks we get messages after any key
    # http: // scrstorage.s3.amazonaws.com / Monosnap_94hrz_2023 - 05 - 27_22 - 01 - 13.
    # png



