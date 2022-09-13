## Урок 2. Знакомство с Python. Продолжение
## **************************************
## 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
## А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
## Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
## Это происходит до тех пор, пока не будет найден палиндром.
## Напишите такую программу, которая найдет палиндром введенного пользователем числа.
## **************************************

## Функция № 1 - Проверка на полиндром: да-нет?
import math
from site import abs_paths


def verify_to_polindrom(input_data):
    # в циклах буду сравнивать по символу слева и справа от середины.
    # при первом же не совпадении - результат не полиндром
    result = True

    if input_data is not str:  # уход от унарных +/-
        input_data_str = str(abs(input_data))
    else:
        input_data_str = str(abs(int(input_data)))

    len_input_data = len(input_data_str)    # длина строки (кол-во цифр в числе)

    if len_input_data == 1:
        return result                       # 1 символ поумолчанию полиндром.

    # решение - движение к середине и сравнение с краёв
    # до середины идём (при нечётной длине - просто центр пропускаем)
    for i in range(0, len_input_data // 2):
        if input_data_str[i] != input_data_str[len_input_data - i - 1]:
            result = False
            break 

    return result

## Функция № 2 - Перевернуть число
def revirse_number(input_data):
    
    result = ""

    if input_data is not str:  # уход от унарных +/-
        input_data = str(abs(input_data))
    else:
        input_data = str(abs(int(input_data)))

    if input_data[0] == '-' or input_data[0] == '+': # унарные + и -
        input_data[0] = ''
    
    len_of_input_data_str = len(input_data)

    if len_of_input_data_str == 1:
        result = input_data
        return result                                    # 1 символ

    list_of_indexis = range(0, len_of_input_data_str)    # список индексов

    for elem in list_of_indexis:
        result += input_data[len_of_input_data_str - elem -1]

    return result # str


### ********* основной код - функция main  ********* 
flag_stop_input_data = False
num_try_input_data = 5
counter = 0
while not flag_stop_input_data and counter < num_try_input_data:
    try:
        number = int(input("Введите число - целое: "))
        flag_stop_input_data = True
        counter += 1
    except:
        print("Вы ввели что-то не то вместо целого числа")

print("Решение:")
flag_stop_find_polindrom = False
while not flag_stop_find_polindrom:
    flag_stop_find_polindrom = verify_to_polindrom(number)
    print(f"Число {number} полиндром? -> {flag_stop_find_polindrom}")
    if not flag_stop_find_polindrom:
        new_number = int(revirse_number(number))
        if new_number != number:
            flag_stop_find_polindrom = verify_to_polindrom(new_number+number)
            print(f"Число {new_number+number} полиндром? -> {flag_stop_find_polindrom}")
        else:
            flag_stop_find_polindrom = True
