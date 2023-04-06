#Задание 3

A = int(input('Введите любое число -> '))
B = int(input(f'Введите любое число больше {A} -> '))
if B < A:
    print("Конец.")
else:
    C = list()
    for i in range(A, B):
        if i % 2 == 0:
            C.append(i)
    print(C)
