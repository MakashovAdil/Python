﻿#1. Пользователь вводит целое число. Выведите его строку-описание вида 
#"отрицательное четное число", "нулевое число", "положительное нечетное число", например, 
#численным описанием числа 190 является строка "положительное четное число". 
#Если число не является четным - выведите сообщение "число не является четным"
a = int(input("Введите целое число -> "))
if a%2 == 0 and a != 0:
    if a<0:
        print("Отрицательное четное число")
    else:
        print("Положительное четное число")
elif a == 0:
    print("Нулевое число")
else:
    if a<0:
        print("Отрицательное нечетное число")
    else:
        print("Положительное нечетное число")

#--------------------------------------------------------------------------------------------------------------------

#2. Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? 
#Гласными называют буквы «a», «e», «i», «o», «u».
#Для решения задачи создайте переменную и в неё положите слово с помощью input()
#А также определите количество каждой из этих гласных букв 
#Если какой-то из перечисленных букв нет - Выведите False

word = str(input("Введите слово -> "))
vowel = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

v = 0
c = 0

a = 0
e = 0
l = 0
o = 0 
u = 0

for i in word:
    if i in vowel:
        v += 1
        if i == 'a':
            a += 1
        elif i == 'e':
            e += 1
        elif i == 'i':
            i += 1
        elif i == 'o':
            o += 1
        elif i == 'u':
            u += 1

    elif i in consonant:
        c += 1

print("Гласных -> ", v)
print("Согласных -> ", c)
print(f'a = {a}')
print(f'e = {e}')
print(f'i = {l}')
print(f'o = {o}')
print(f'u = {u}')