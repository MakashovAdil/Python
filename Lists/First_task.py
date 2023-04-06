#Задание 1

N = int(input('Введите число строк -> '))
a = 0
list = []
while a != N:
    M = input(f'Введите {N} числа от 2 и до 10000 -> ')
    list.append(M)
    a += 1
print(*list[::-1])