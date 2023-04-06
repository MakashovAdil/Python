#Задание 1

N = int(input("Введите число -> "))
if N == 0:
    print("Конец.")
elif N == 1:
    a = input(f"Введите {N} число")
elif 1<N<5:
    a = input(f"Введите {N} числа подряд")
else:
    a = input(f"Введите {N} чисел подряд")

numbers = list(a)

zeros = 0
for num in numbers:
    if num == "0":
        zeros += 1 
    else:
        zeros += 0
print(zeros)