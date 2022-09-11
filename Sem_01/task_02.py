# **************************************
# Задание 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# **************************************
# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#       x  y  z
#  i\j  0  0  0   И  =  И
#       0  0  1   Л  =  Л
#       0  1  0   Л  =  Л
#       0  1  1   Л  =  Л
#       1  0  0   Л  =  Л
#       1  0  1   Л  =  Л
#       1  1  0   Л  =  Л
#       1  1  1   Л  =  Л
# m * n  - > 8 * 3  = 24
# Решение

# ********* Определение функций ********* 
b = [0,  0,  0,  0,  0,  1, 0,  1,  0, 0,  1,  1, 1,  1,  1,  1,  0,  0, 1,  0,  1, 1,  1,  0]
sizeB = len(b)
column = 3
i = 0                          # счётчик, чтоб бегать по набору/кортежу из трёх значений
x, y, z = False, False, False  # для простоты понимания ввожу лишние переменные
boolValueLeft = False          # результат левого выражения: ¬(X ⋁ Y ⋁ Z)
boolValueRight = False         # результат правого выражения: ¬X ⋀ ¬Y ⋀ ¬Z
boolResult = True              # храним результат выражения: boolValueLeft==boolValueRight
#!флаг boolResult для выхода при первом невыполенении равенства и хранения результата выполнения
while(boolResult and i < sizeB/column): 
    if(b[i*column]==1):   # 1й столбец матрицы условной двухмерной
        x = True     # так как and or - это логические (булевы) и или, 
    else:            # то перменные должны быть:  False, True. С другим не сработает (т.е. с 1 и 0)
        x = False
    if(b[i*column+1]==1): # 2й столбец матрицы условной двухмерной
        y = True
    else:
        y = False  
    if(b[i*column+2]==1): # 3й столбец матрицы условной двухмерной
        z = True
    else:
        z = False 
    boolValueLeft = not(x or y or z)              # ¬(X ⋁ Y ⋁ Z)
    boolValueRight = not(x) and not(y) and not(z) # ¬X ⋀ ¬Y ⋀ ¬Z
    print(f'Кортеж {i}: [{b[i*column]}, {b[i*column+1]}, {b[i*column+2]}] -> {boolValueLeft} = {boolValueRight}')
    if(boolValueLeft != boolValueRight):
         boolResult = False  
    i += 1
print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z', end = "  ->  ")
if boolResult:
    print('Истинно')
else:
    print('Ложно')