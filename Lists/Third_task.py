#Задание 3

m = int(input('Максимальная масса, которую может выдержать одна лодка -> '))
n = int(input('Кол-во рыбаков -> '))

a = 0 
adv = 1
ves = []
while a != n:
    ai = int(input(f'Вес путешественника номер {adv} -> '))
    ves.append(ai)
    a += 1
    adv += 1

answer = 0
for i in ves:
    answer += i

total = answer/m
if total > int(total):
    total += 1

print(f'Для того чтобы переправить {n} рыбаков на противоположный берег нужно {int(total)} лодок')