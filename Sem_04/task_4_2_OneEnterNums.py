# 2 - Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности. 
# Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

def input_list_of_nums(output_string):
    '''
    Данный метод рекурсивно предлгагает пользователю корректно ввести список
    Рекурсия, чтоб не использовать цикл
    '''
    result = []
    bool_need_reinput = True
    try:
        result = list(map(int, input(output_string).split()))        
        assert len(result) > 1, "Вы не ввели список, нужно ввести не менее 1 числа!" # от обратного
        bool_need_reinput = False 
    except AssertionError as err:   
        print(err)                             
    except:                                                               
        print("Ошибка при вводе списка из чисел!")
    else:
        # print("\tУспешно введён список из чисел.")
        print('')
    finally:
        if bool_need_reinput:
            result = input_list_of_nums(output_string)
    return result

def get_list_single_entry_nums(input_list):
    '''
    Возвращает список неповторяющихся элементов исходного списка 
    '''
    result = []
    if len(input_list) > 1:
        for i, item in enumerate(input_list):
            if item not in result:
                result.append(item) # result.append(input_list[i])
    elif len(result) ==  1:
        result = input_list
    return result

### ********* основной код - функция main  ********* 
output_string = "\nВведите список через пробел и нажмите enter: \n список -> "
list_of_nums = input_list_of_nums(output_string)
result_list = get_list_single_entry_nums(list_of_nums)
print(f"Результат:\n{list_of_nums} -> {sorted(result_list)}")



