#3 Задание

N = input("Введите числа через пробел -> ")
a = N.split()
b = set()
for i in a:
    print(i)
    if i in b:
        print("YES")
        b.add(i)
    else:
        print("NO")
        b.add(i)