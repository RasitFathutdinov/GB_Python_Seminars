# # 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов в виде списка
# # *Пример:*
# # - Для N = 5: 1, -3, 9, -27, 81
# # (-3)**(i-1) i от 0 до N-1

# N = int(input("Введите число: "))
# print(f"Для N={N} -> ", end= "")
# for i in range(0,N-1):
#     print((-3)**i, end= ", ")
# else:
#     print((-3)**(N-1))


# # 2.Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами
# A = [1, 2, 3, 8, 9, 10]
# sum = 0
# poz_min = 0
# poz_max = 0
# i = 1
# size = len(A)
# while i < size:
#     if A[i] > A[poz_max]:
#         poz_max = i
#     elif A[i] < A[poz_min]:
#         poz_min = i   
#     i += 1
# print(poz_min, poz_max)
# if poz_max > poz_min:
#     for i in range(poz_min, poz_max+1):
#         sum = sum + A[i]
# elif poz_max < poz_min:
#     for i in range(poz_max, poz_min+1):
#         sum = sum + A[i]   
# else:
#     sum = A[poz_max]
# print(A, sum)


# # 3.Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10% ( 10% от наибольшего)
# # [4, 5, 1, 6, 2, 8]
# # [4,5,8,6,2,1]

# A = [2, 3, 6, 98, 56, 45, 78, 100, 49]
# max = A[0]
# for i in A[1:]:
#     if i > max:
#         max = i
# count = 0
# for i in A:
#     if  max*0.9 < i and i !=max:
#         count += 1 
# print(count)



## ********************* РЕШЕНИЯ ДРУГИХ ЗАЛОВ ********************* 
## ********************* РЕШЕНИЯ ДРУГИХ ЗАЛОВ ********************* 
## ********************* РЕШЕНИЯ ДРУГИХ ЗАЛОВ ********************* 

# from random import randint

# list = []
# def create_list():

#      for x in range(0, 10):
#          list.append(randint(0, 99))

#      print(list)
#      return list

# def find_distance_result(array):
#     minimal_digit = min(array)
#     maximal_digit = max(array)

#     min_index = array.index(minimal_digit)
#     max_index = array.index(maximal_digit)

#     summa = 0
#     if min_index < max_index:
#         i = min_index + 1
#         while i < max_index:

#             summa += array[i]
#             i += 1
#     else:
#         i = min_index - 1
#         while i > max_index:
#             summa += array[i]
#             i -= 1

#     print(summa)

# find_distance_result(create_list())


# n=int(input('введите N '))
# i=0
# number=0
# while i<n:
#     number = (-3)**i
#     print (number, end=' ')
#     i=i+1





# def return_list(n):
#     list = [1]
#     temp = 1
#     while(n > 1):
#         temp = temp * (-3)
#         n = n-1
#         list.append(temp)
#     print(list)


# return_list(int(input('Введите число: ')))

# t = (28, 9, 1990)
# print(type(t), t)
# # print(t)
# colors = ['red', 'green', 'blue']
# print(type(colors), colors) # ['red', 'green', 'blue']

# t = tuple(colors)
# print(type(t), t) # ['red', 'green', 'blue']


# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 

# Пример:
# 67.82 -> 23
# 0.56 -> 11

# # определение функции
# def sum_elem(num2, num):  # нахожу сумму элементов
#    my_sum = 0
#    i = 0
#    list_len = len(num2)
#    #print(i, my_sum, list_len)
#    while i < list_len:
#       my_sum = my_sum + num2[i]
#       #print(i, my_sum, num2[i])
#       #print(type(i), type(my_sum), type(num2[i]))
#       i += 1
#    print(f'{num} -> {my_sum}')

# # основной код
# num = (input('Введите вещественное число: '))
# num2 = list(num)  # делаю список
# num2.remove('.') # удаляю точку

# for i in range(len(num2)):
#     num2[i] = int(num2[i])  # изменяю строки на числа
# print(num2)

# sum_elem(num2, num) # вызов ранее определённой функции




# def sum_elem(num2):  # нахожу сумму элементов
#    my_sum = 0
#    i = 0
#    list_len = len(num2)
#    print(i, my_sum, list_len)
#    while i < list_len:
#       my_sum = my_sum + num2[i]
#       print(i, my_sum, num2[i])
#       print(type(i), type(my_sum), type(num2[i]))
#       i =+ 1
#    print(f'{num2} -> {my_sum}')
