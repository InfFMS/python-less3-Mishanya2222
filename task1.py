#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.
g = 0
while True:
    a = float(input('ввведите число'))
    if a > 0:
        g = g+1
    elif a == 0:
        break
print(g)