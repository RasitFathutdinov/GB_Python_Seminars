# 3 - В файле, содержащем фамилии студентов и их оценки,
# изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».
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

try:
    somefile = open("data_of_students.txt", "rt", encoding='utf-8')
    lines = somefile.readlines()
    somefile.close()
    if lines != None:
        for i, line in enumerate(lines): # удаление всех разделителей справа
            lines[i] = lines[i].rstrip()
            if int(lines[i][-1]) > 4:
                lines[i] = lines[i].upper() + "\n"
            else:
                lines[i] = lines[i] + "\n"

        somefile = open("data_of_students.txt", "wt", encoding='utf-8')
        somefile.writelines(lines)
        somefile.close()

except Exception as ex:
    print(ex)

# with open("task_4_3_data_of_students.txt", 'wt', encoding='utf-8') as file:
#         lines = file.readline()
# print(lines)

# output = open("task_4_3_data_of_students.txt", 'w')
# output.writelines(lines)
# output.close()


# # читает все строки в файле и возвращает их в виде списка 
# # (при этом завершающие символы новой строки остаются на своих местах):
# file_object = open("myfile", 'r')
# print(len(file_object.readlines()))
# file_object.close()

# # Если в файле не осталось данных, которые можно было бы прочитать, 
# # readline возвращает пустую строку, что позволяет (например) 
# # легко подсчитать количество строк в файле:
# file_object = open("myfile", 'r')
# count = 0
# while file_object.readline() != "":
#     count = count + 1
# print(count)
# file_object.close()

# # укажите newline="\n", "\r" или "\r\n", 
# # в результате чего только эта последовательность будет использоваться 
# # как признак новой строки:
# input_file = open("myfile", newline="\n")
# >>> try:
# ... fout = open('relativity', 'xt')]
# ... fout.write('stomp stomp stomp')
# ... except FileExistsError:
# ... print('relativity already exists!. That was a close one.')