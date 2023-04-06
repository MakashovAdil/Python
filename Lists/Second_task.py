#Задание 2

N = int(input('Введите кол-во чисел -> '))
list = [x for x in input().split()]

a = 0
b = 0
i = 0
while a != N:
    list[i] = N-b
    i += 1
    b += 1
    a += 1
print(*list)