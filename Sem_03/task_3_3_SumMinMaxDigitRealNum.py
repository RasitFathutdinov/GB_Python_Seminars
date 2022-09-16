# ## Урок 3. Данные, функции и модули в Python
# ## 3-Задайте список из вещественных чисел. 
# ## Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# ## Пример:
# ## [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# ## [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
# ## Решение

# ## Примечание !!! сбой в вычислениях при единице в первом разряде !!!

# ## ********* Определение функций ********* 
# ## Функция № 1 - Поиск количества знаков после запятой
def get_num_preсision(number):
    result = 0
    epsilon = 10 ** (-9)
    #print(result, number)
    while abs(number % 1) > epsilon:
        number *= 10
        result += 1
        print(result, number)
    return result

# ## Функция № 2 - Поиск разряда целой части
def get_integer_part_digits_count(number):
    result = 0
    while number // 1:
        number /= 10
        result += 1
        #print(result, number)
    return result

# ## Функция № 3 - Поиск дробной части и возврат в дробном виде (если разделить на 10^precision, то в дробной части)
def get_fractional_part(number):
    epsilon = 10 ** (-6)
    precision = get_num_preсision(number)
    #print(number, '  -  ', number % 1)
    result = int((number % 1) * (10 ** precision))
    if -epsilon < result < epsilon:
        result = 0 
    return result * 10 ** (-precision)

# ## Функция № 4 - Поиск целой части
def get_integer_part(number):
    result = 0
    counter = 0
    number = int(number)
    #print(number, "  -----")
    while number % 10:
        result += (number % 10) * (10 ** counter)
        counter += 1
        number //= 10
        #print(result, counter, number)
    return result

# ## Функция № 5 - Сумма максимальной и минимальной дробной части чисел в списке
def find_sum_min_maxt(input_list, my_swich):
    temp_val = get_integer_part(input_list[0])
    temp_val = input_list[0] - temp_val
    #print("temp_val -> ", temp_val)
    min_fract_part = temp_val
    max_fract_part = temp_val
    max_precition = get_num_preсision(input_list[0])
    result = 0

    for elem in input_list[1:]:
        temp_val = get_integer_part(elem)
        temp_val = elem - temp_val
        #print("temp_val -> ", temp_val)
        if max_fract_part < temp_val:
            max_fract_part = temp_val
        elif min_fract_part > temp_val:
            min_fract_part  = temp_val
            max_precition =get_num_preсision(input_list[0])

    result = round(max_fract_part - min_fract_part, max_precition)
    if my_swich == 1:
        result = int(result * 10 ** max_precition)
    return result

# ## ********* основной код - функция main  ********* 
output_string = "\nВведите список через пробел и нажмите enter: \n список -> "
try:
    list_of_real_nums = list(map(float, input(output_string).split()))
    if len(list_of_real_nums) < 2:                                   
        print("Вы не ввели список, нужно ввести не менее 1 числа!")  
        float('-')                                                    
except:                                                              
    print("Ошибка при вводе списка из чисел!")
else:
    print("\nУспешно введён список из чисел.\nРезультат выполнения программы:")
    # Формат. вывод: [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
    print(list_of_real_nums, " => ", find_sum_min_maxt(list_of_real_nums, 1), ' или ', find_sum_min_maxt(list_of_real_nums, 2), '\n')


