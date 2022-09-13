# ## Урок 2. Знакомство с Python. Продолжение
# ## **************************************
# ## 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# ## Учтите, что числа могут быть отрицательными
# ## Пример:
# ## 67.82 -> 23
# ## 0.56 -> 11
# ## **************************************

# ## Решение
# ## Так как числа вещественные, то буду решать в 2 этапа:
# ## - выделяю целую часть
# ## - выделяю дробную часть
# ## - считаю сумму сумм цифр дробной и целой части

# ## решение через строки, так как при делении на % 1 много знаков после запятой 
# ## (и опять нужно будет считать кол-во символов после запятой в водимой строке/числе и запаминать)

# ## ********* Определение функций ********* 
# # Функция № 1 - Ввод вещественного числа 
# def input_number_str_format():
#     result = input("Введите вещественное число и нажмите enter: ")
#     return try_convert_str_to_float_with_reinput(result)

# # Функция № 2 - Попытка конвертировать, если неудачно, то рекурсивно заново вводим
# def try_convert_str_to_float_with_reinput(input_string):
#     # условие для останова корректного ввода вещественного числа
#     flag_stop_input_data = False
#     # лишняя и занимающая память переменная, но это для понимания, чтоб не возвращать input_string
#     result = input_string
#     while not flag_stop_input_data:
#         try:
#             # если введено не чиcло (вещественное), то интерпрититор выдаст исключение при приобразовании строки
#             temp = float(result)
#             flag_stop_input_data = True  # если сработает исключение, то приращения флаг на выход не меняется!
#                                          # и придётся заново повторять ввод данных
#         except:
#             print("\t! Введено не вещественное число, либо в числе \',\' вместо \'.\'. Повторите ввод !")
#             result = input_number_str_format()
#     return result

# # Функция № 3 - Получить целую и дробную часть числа в виде списка из 2х элементов
# def get_int_and_fract_part_of_number(input_string):
#     # вызываю 2 раза, поэтому решил съэкономить время исполнения на прогон цикла подсчёта количества символов
#     count_of_symbols = len(input_string)
#     # при наличии унарных знаков, избавляемся от них
#     if input_string[0] == '+' or input_string[0] == '-':
#         input_string = input_string[1 : count_of_symbols]
#         count_of_symbols -= 1
#     # поиск позиции разделителя дробной и целой части
#     position_of_point = input_string.find('.')
#     # динамически выделяю память под список, чтоб потом в него добавлять
#     result = []
#     # поисk и сохранение целой и дробной части соответсвенно
#     if position_of_point != -1:     # если пользователь ввёл число c дробной частью (в матемтике N подмножество R)
#         integer_part = int(input_string[0 : position_of_point])
#         fractional_part = int(input_string[position_of_point + 1 : count_of_symbols])
#         result.append(integer_part)
#         result.append(fractional_part)
#     else:                           # если пользователь ввёл число без дробной части (в матемтике N подмножество R)
#         result.append(int(input_string))
#         result.append(0)
#     return result

# # Функция № 4 - Подсчёт сумм цифр числа (целое - есть частный случай вещественного)
# def get_sum_digits_of_number(left_part, right_part = 0):
#     result = 0

#     if left_part != 0: 
#         while left_part % 10: # подсчёт суммы цифр от целой части числа
#             result += left_part % 10
#             left_part = left_part // 10
#         else:
#             result += left_part

#     if right_part != 0: 
#         while right_part % 10: # подсчёт суммы цифр от дробной части числа
#             result += right_part % 10
#             right_part = right_part // 10
#         else:
#             result += right_part

#     return int(result)

# ## ********* основной код - функция main  ********* 
# real_number_in_str_format = input_number_str_format()
# int_fract_part_number = get_int_and_fract_part_of_number(real_number_in_str_format)
# ## 67.82 -> 23 
# print(real_number_in_str_format, " -> ", end = '')
# print(get_sum_digits_of_number(int_fract_part_number[0], int_fract_part_number[1]))