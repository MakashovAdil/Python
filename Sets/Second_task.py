#2 Задание

N1 = input("Введите числа через пробел -> ")
N2 = input("Введите числа через пробел -> ")
a = N1.split()
b = N2.split()
m1 = set(a)                                   
m2 = set(b)
one = m1.union(m2)
print(one)