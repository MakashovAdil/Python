#2 Задание

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
