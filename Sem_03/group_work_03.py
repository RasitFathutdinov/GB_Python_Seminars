
# Задания с семинара:
# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3
# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
# 3.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}




# # 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# # ['апап4', 'fdgg3', 'fgdf', '6', 'fg24'] - ищем 24 - найдено на 4 индексе

# list_of_str = ['апап4', 'fdgg3', 'fgdf', '6', 'fg24']

# number = int(input("Введите число: "))  # чисто для ошибки в переводе

# position_of_number = -1
# tem_position = -1
# counter = 0

# # for elem in list_of_str:
# #     tem_position = elem.find(str(number))
# #     if tem_position != -1:
# #         position_of_number = tem_position
# #         break
# #     counter += 1

# # if tem_position != -1:
# #     print(list_of_str, f"искали {number} -> его позиция", counter)
# # else:
# #     print(list_of_str, f"искали {number} -> а его нет! ")








# # data = ['апап4', 'fdgg3', 'fgdf', '6', 'fg24']
# # count = 0
# # for i in data:
# #     if '24' in i:
# #         print([i], count)
# #     count += 1


# # 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# # *Пример:*
# # - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# # - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# # - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# # - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# # - список: [], ищем: "123", ответ: -1

# # list_of_anytypes1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]          #, ищем: "qwe", ответ: 3
# # list_of_anytypes2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]   #, ищем: "йцу", ответ: 5
# # list_of_anytypes3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]          #, ищем: "йцу", ответ: -1
# # list_of_anytypes4 = ["123", "234", 123, "567", 123.5]                      #, ищем: "123", ответ: -1
# # list_of_anytypes5 = []                                              #, ищем: "123", ответ: -1

# user_sub_str = input("Введите строку: ")  # чисто для ошибки в переводе

# def find_my_substring(list_of_anytypes, my_substring):
#     position_of_number = -1
#     tem_position = -1
#     counter = 0
#     counter2 = 0
#     for elem in list_of_anytypes:
#         if (type(elem)) is str:
#             tem_position = elem.find(str(my_substring))
#             if (list_of_anytypes[counter] != my_substring) and (counter2 == 1):
#                 position_of_number = tem_position
#                 break
#         else:
#             continue
#         counter += 1
        
#     if tem_position != -1:
#         print(list_of_anytypes, f"искали {my_substring} -> его позиция", counter)
#     else:
#             print(list_of_anytypes, f"искали {my_substring} -> а его нет! ")
#     return counter














# data = ["123", "234", 123, "567"]

# def second(data, qwe):
#     count = 0
#     count2 = 0
#     for i in data:
        
#         if "123" == i:
#             count2 += 1
#         if count2 > 1:
#             return count
#         count += 1
#     return -1    
# print(second(data, "123"))


# # 3.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# #  Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# # number = int(input('Введите число: '))

# # slovar = {}
# # i = 1
# # while i <= number:
# #     slovar[i] = 3 * i + 1

# #     i += 1

# # print(slovar)






















