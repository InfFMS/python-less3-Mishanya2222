# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".
def resheto(N):    # Решето эратосфена
    primes = [i for i in range(N + 1)]
    primes[1] = 0
    i = 2
    while i <= N:
        if primes[i] != 0:
            j = i + i
            while j <= N:
                primes[j] = 0
                j = j + i
        i += 1

    return [i for i in primes if i != 0]
n=int(input())
if n==0:
    print('Введите число!')
else:
    lst=list(map(int, input().split()))
    ma=max(lst)

    
    simple=resheto(ma)
    max_simple=0
    min_simple = ma+1
    for num in lst:
        if num in simple:
            if num>max_simple:
                max_simple=num
            elif num<min_simple:
                min_simple = num
    if max_simple==0:
        print('Нет простых чисел')
    else:
        print(max_simple, min_simple)


