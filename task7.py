def Fibonach(n):
    list_fi=[1, 1]
    i, j=0, 1
    while list_fi[i]+list_fi[j]<=n:
        list_fi.append(list_fi[i]+list_fi[j])
        i+=1
        j+=1
    return list_fi

# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное из введённых чисел Фибоначчи.
# Вывести "нет", если чисел Фибоначчи в последовательности нет.
# Числа Фибоначчи – это последовательность чисел,
# которая начинается с двух единиц и каждое следующее число
# равно сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13, …

a=int(input())
lst=[]
ma=0
while a!=0:
    if a>ma:
        ma=a
    lst.append(a)
    a=int(input())
list_fi=Fibonach(ma)
min_fi=ma+1
for num in lst:
    if num in list_fi and num<min_fi:
        min_fi=num
if min_fi==ma+1:
    print('нет')
else:    
    print(min_fi)  
