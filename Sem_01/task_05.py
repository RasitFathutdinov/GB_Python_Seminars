# **************************************
# Задание 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21 
# **************************************

# ********* Определение функций ********* 
# Функция № 1 - Ввод координат точки, поумолчанию 2х-мерное пространство
def input_coord_of_point(damange = 2):
    point = []
    i = 0
    while i < damange:
        try:
            # если введено не чило (вещественное), то интерпрититор выдаст исключение при приобразовании строки
            point.append(float(input(f"Введите координату # {i+1} (1 - ось Оx, 2 - ось Оy и т.д.): ")))
            i += 1  # если сработает исключение, то приращения счётчика не будет!
                    # и придётся заново повторять ввод данных
        except:
            print("\t! Введено не число. Повторите ввод !")
    return point

# Функция № 2 - Растояние между точкам в n-мерном пространстве (поумолчанию двухмерное)
def calc_distance_in_space(point_one, point_two, damange = 2):
    result = 0.0
    for i in range(0, damange):
        result += (point_one[i] - point_two[i]) ** 2
    return result ** 0.5
    
# Функция № 3 - Вывод координат точки, поумолчанию 2х-мерное пространство
def print_point(point, damange = 2):
    list_of_iteration = range(0, damange-1)  # создаю индексы отдельно, чтоб при каждой итерации 
    print("(", end = "")                               # не создавать снова
    for i in list_of_iteration:
        print(point[i], end = "; ")
    else:    # чтоб форматированно вывести последнюю координату без ;
        print(point[i+1], end = ")")
    return

# ********* основной код - функция main  ********* 
damange_of_space = 2     # размерность пространства, по умолчанию 2D
# ввод координат 2-х точек через вызов функции 1
print("Введите координаты первой точки (А)" )
point_a = input_coord_of_point()
print("Введите координаты второй точки (B)" )
point_b = input_coord_of_point()
# форматированный вывод под условия: A (7,-5); B (1,-1) -> 
# для такого выводв хорошо бы сделать метод point -> string
# но делаю в лоб
print(f"Расстояние между точками в {damange_of_space}D пространстве:" )
print("A ", end = "")
print_point(point_a)
print("; B", end = "")
print_point(point_b) 
print(" -> ", end = "")
# расчёт расстояния между 2-мя точками через вызов функции 2
print(f"{calc_distance_in_space(point_a, point_b):9.2f}")