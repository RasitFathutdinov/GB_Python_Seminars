
# ## Урок 3. Данные, функции и модули в Python
# ## **************************************
# ## 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# ## Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# ## Пример:
# ## [2, 3, 4, 5, 6] => [12, 15, 16];
# ## [2, 3, 5, 6] => [12, 15]
# # ## Решение

# # ## ********* Определение функций ********* 
# # ## Функция № 1 - Произведение пар чисел от краёв к середине
# def get_half_list_with_product_nums(list_of_nums):

#     len_of_list = len(list_of_nums)
#     len_of_list_is_odd = False
#     result = []                         # пустой список, сюда буду добавлять произведение пар

#     if len_of_list > 0:                 # если передан пустой список - то и возврат пустого списа
#         if len_of_list % 2:             # -> 1 - если длина списка нечётная
#             len_of_list_is_odd = True
        
#         for i in range(0, len_of_list // 2):
#             result.append(list_of_nums[i] * list_of_nums[len_of_list - i - 1])
#         else:
#             if len_of_list_is_odd:      # -> если длина списка нечётная, то срединный сам на себя
#                 result.append(list_of_nums[i+1]*list_of_nums[i+1])
    
#     return result

# # ### ********* основной код - функция main  ********* 
# output_string = "\nВведите список через пробел и нажмите enter: \n список -> "
# try:
#     input_list = list(map(int, input(output_string).split()))         # поумолчанию split() по пробелам
#     if len(input_list) < 2:                                           # чтоб не распылять метод, проверяю наличие списка
#         print("Вы не ввели список, нужно ввести не менее 1 числа!")   # по хорошему ф-я get_half_list_with_product_nums дожна возвращать
#         int('-')                                                      # список result = [[new_list], [res_of_running]] 
# except:                                                               # new_list - результат, res_of_running: 1 при ОК, 0 при 1 элементе (нет нечётых), -1 при отсутсвии списка
#     print("Ошибка при вводе списка из чисел!")
# else:
#     print("\nУспешно введён список из чисел.\nРезультат выполнения программы:")
#     # Формат. вывод: [2, 3, 5, 6] => [12, 15]
#     print(input_list, " => ", get_half_list_with_product_nums(input_list), '\n')

