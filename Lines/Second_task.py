#2 Задание

txt = input("Введите строку, длина которой не превосходит 1000 -> ")
if len(txt) > 1000:
    print("Конец.")
else:
    a = " ".join(txt.split())
    print(a)
