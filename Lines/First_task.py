#1 Задание

txt = input("Введите строку без пробелов -> ")
text = txt.lower()
txet = text[ : : -1]
if text == txet:
    print("Yes")
else:
    print("No")