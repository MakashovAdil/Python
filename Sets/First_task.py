#1 Задание

N = int(input("Введите кол-во чисел -> "))
if N == 0 or N > 100000:
    print("Конец.")
else:
    M = input(f"Введите {N} чисел через пробел -> ")
    a = set(M.split())
    print(a)