# 1 - Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.
# a = str(input("Введите числа через пробел: "))
# list_of_str = a.split(" ")
# print(list_of_str)
# list_of_num = []
# for i in list_of_str:
#     list_of_num.append(int(i))
# min = list_of_num[0]
# max = min
# for i in list_of_num:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# print(min, max)




# ****************************

# line = '1, 2, 3, 4, 5'
# list = []

# for i in range(len(line)):
#     if line[i] != ',' and line[i] != ' ':
#         list.append(int(line[i]))

# print(*list)
# print(f'Min: {min(list)}')
# print(f'Max: {max(list)}')


# 2 - Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел.
#  НОК - наименьшее общее кратное, которое делится и на первое, и на второе число.

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# def NOD(a,b):
#     if a % b == 0:
#         return b
#     elif b % a == 0:
#         return a
#     elif a > b:
#         return NOD(a%b, b)
#     else:
#         return NOD(b%a, a)


# def NOK(a, b):
#     return  a*b / NOD(a, b)
# print(int(NOK(a, b)))


# Решение №2

# i = min(a, b)
# while True:
#     if i % a == 0 and i % b == 0:
#         break
#     i += 1
# print(i)


# ***********************************

#  my_str=(1,вапа,4,5,6)
# print(*my_str, sep=" ")

# max_value=max(my_str, key=lambda i: int(i))
# min_value=min(my_str, key=lambda i: int(i))

# print(max_value)
# print(min_value)


# 3 - Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Число N вводится пользователем. 
# Позиции хранятся в файле file.txt в одной строке одно число
# Позиции в файл вам нужно программно положить в файл в зависимости от выбранного N: 
#     если пользователь введет двойку, то в файле вряд ли будут индексы 5 или 16.
# В решении должны быть и запись в файл, и чтение из файла.

# 5 =>  [-4, 3, -1, 2, 0]




# ****************************************
# ДЗ


# Урок 4. Данные, функции и модули в Python. Продолжение
# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.