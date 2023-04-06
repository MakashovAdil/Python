#1 Задание

def factorial(x):
    int(x)
    f1 = 1
    a = x
    while a != 0:
        f1 *= a
        a -= 1
    print(f1)
    f2 = 1
    b1 = []
    for i in range(f1+1):
        c = 1
        while i != 0:
            c *= i
            i -= 1
        b1.append(c)
    b1.pop(0)
    b2 = b1[::-1]
    print(b2)

print(factorial(3))