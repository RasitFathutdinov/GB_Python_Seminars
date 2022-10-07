# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, 
# написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

def get_list_of_tuple(list1: list, list2: tuple) -> list: 
    # list3 = []
    # for i in range(len(list1)):
    #     list3.append(tuple([list2[i], list1[i]]))
    return list(zip(list2, list1))

print("**************** Списки **************")
list1 = ['Python', 'C++', 'C#', 'Pascal', 'Basic', 'Fortran', 'Algol', 'Ada']
list2 = list(range(1, len(list1)+1))
list3 = get_list_of_tuple(list1, list2)
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}")

# удаление без формирования нового списка - обход сзади
counter = len(list3) # переменная len в объекте list3 класса список будет меняться с удалением
while counter > 0:
    sum = 0
    counter -= 1
    index_list = counter
    elem = list3[index_list]                # кортеж
    for index_tumpl in range(len(elem[1])): # подсчёт суммы очков: кодов букв строки в кортеже
        sum += ord((elem[1])[index_tumpl])
    if sum % (elem[0]) == 0:                # первый элемент кортежа в делитялх у суммы очков
        list3[index_list] = tuple([sum, list1[index_list]]) # замена элемента списка
    else:
        del list3[index_list]
print("**************** После обработки **************")
print(f"list3 = {list3}")
