# 1 - Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

# https://gbcdn.mrgcdn.ru/uploads/record/211579/attachment/4f70fd8457485a144c5d934b717f73b3.mp4

import re


def get_all_multipliers(input_number):
    '''
    возращает все возможные множители 
    (поиск при константном значении числа входного)
    разложение на множители
    '''
    result = [1]
    if input_number > 1:
        for i in range(2, input_number):
            if input_number % i == 0:
                result.append(i)
    return result

def get_basic_multipliers(input_number):
    '''
    возращает только базовые множители 
    (поиск с уменьшением числа на этот множитель)
    разложение на множители
    '''
    result = [1]
    if input_number > 1:
        counter = 2
        while input_number != 1:
            if input_number % counter == 0:
                result.append(counter)
                input_number /= counter 
            else:
                counter += 1
    return result

def get_basic_multipliers_single_entry(input_number):
    '''
    возращает только базовые неповторяющиеся множители 
    (поиск с уменьшением числа на этот множитель)
    разложение на множители
    '''
    result = [1]
    if input_number > 1:
        counter = 2
        while input_number != 1:
            if input_number % counter == 0:
                if counter not in result:
                    result.append(counter)
                input_number /= counter 
            else:
                counter += 1
    return result

def num_is_simple(input_number):
    '''
    Простое число — натуральное число, имеющее ровно два различных натуральных делителя. 
    Другими словами, натуральное число p является простым, если оно отлично от 1 
    и делится без остатка только на 1 и на само p
    '''
    if input_number == 2: # первое простое => сразу возврат истина
        result = True
    elif input_number > 2:
        result = True
        for divider in range(2, input_number):
            if input_number % divider == 0:
                result = False  # при первом же делении нацело возвращаем не простое
                break
    else:
        result = False  # 1 и отрицательные не простые
    return result

def get_simple_multipliers_list(input_number):
    '''
    Функция получает список и возвращает либо пустой либо список из простых множителей
    Вызов функций: "разложение на множители" и "проверку на простое число"
    '''
    result = []
    list_of_single_entry_mult = get_basic_multipliers_single_entry(input_number) # "разложение на множители" 
    len_list = len(list_of_single_entry_mult)
    if len_list == 1:
        if num_is_simple(int(list_of_single_entry_mult[0])):
            result = list_of_single_entry_mult
    if len_list > 1:
        counter = -len_list
        while counter <= -1:
            if not num_is_simple(list_of_single_entry_mult[counter]): # "проверка на простое число"
                del list_of_single_entry_mult[counter]                # нет, так удаляем
            counter += 1
        result = list_of_single_entry_mult
    return result
try:
    number = int(input("Введите натуральное число: "))
    if number <= 0:
        raise ValueError("Несоответствующее значение")
except ValueError as error:
    print(f"Некорректный ввод, введено число меньше 1")
except:
    print("Ошибка при преобразовании в число целого типа")
else:
    list_sample_nums = get_simple_multipliers_list(number)
    print(f"Простые множители числа {number}: {list_sample_nums}")
finally:
    print("Завершено выполнение программы...")