# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.

g = 0
t = 0
while True:
    a = float(input("введите числа"))
    if a // 10>0 and a//10 <10:
        g = g+1
    elif a == 0:
        break
    else:
        t = t+ 1

print(t,'- это другие числа', g,"-это числа двузначные натуральные", end="")