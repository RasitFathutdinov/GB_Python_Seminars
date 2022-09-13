## Урок 2. Знакомство с Python. Продолжение
## **************************************
## 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
## Не используйте функцию math.factorial.
## Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
## Пример:
## - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
## **************************************

# # Функция № 1 - Ввод целого числа
# def input_number():
#     # Цикл использован для проверки корректного ввода целого числа через системные исключения
#     flag_stop_input_data = False
#     while not flag_stop_input_data:
#         try:
#             # если введено не число (или вещественное), 
#             # то интерпрититор выдаст исключение при преобразовании строки
#             number_in_str = input("Введите натуральное число: ")
#             temp_for_call_exception = float(number_in_str)  # чисто для генрации исключения если не Ок по вводу
#             if ('.' in number_in_str or temp_for_call_exception < 0.00000000001 ):
#                 print("\t! нужно было ввести натуральное число !")
#                 float('-')
#             flag_stop_input_data = True  
#             result = int(number_in_str)
#         except:
#             print("\t! Некорректный ввод для целочисленного типа данных. Повторите ввод !")
#     return result

# # Функция № 2* - Факториал через рекурсию
# def factorial_recursive(number):
#     if number == 0:
#         return 1 
#     return number * factorial_recursive(number-1)

# # Функция № 3 - Генерация списка всех факториалов чисел от 1 до number с шагом 1
# def get_array_of_factorials(number):
#     result = [1]                           # array_of_factorials = [ 1, 2, 6, 24 ] ~ (1, 1*2, 1*2*3, 1*2*3*4)
#     for i in range(1, number):
#         result.append((i+1) * result[i-1]) # добавляю в конец списка новый элемент (рост списка справа)
#     return result

# ## ********* основной код - функция main  ********* 
# N = input_number()
# array_of_factorials = get_array_of_factorials(N)
# ## N = 4, тогда [ 1, 2, 6, 24 ]
# print(f"\tN = {N} -> {array_of_factorials}")
