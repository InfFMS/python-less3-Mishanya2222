# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".
n=int(input())
if n==0:
    print('Введиет число')
else:
    mi=100
    ma=0
    count = 0
    for _ in range(n):
        a=int(input())
        if a>9 and a<100 and a%3==0:
            count += 1
            if a > ma:
                ma = a
            if a < mi:
                mi = a


    if count==0:
        print('нет')
    else:
        print(f'Макс:{ma}, Мин:{mi}')
