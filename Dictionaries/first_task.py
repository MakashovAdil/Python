#1 Задание

pets = {
    input('Имя питомца -> '): {
        "Вид питомца": input('Вид питомца -> '),
        "Возраст питомца": int(input('Возраст питомца -> ')),
        "Имя владельца": input('Имя владельца -> ')
        }
}

age = ''

if list(pets[list(pets.keys())[0]].values())[1] % 10 == 1:
  age = 'год'
elif list(pets[list(pets.keys())[0]].values())[1] % 10 in [2, 3, 4]:
  age = 'года'
else:
  age = 'лет'

print(f'Это {list(pets[list(pets.keys())[0]].values())[0]} по кличке "{list(pets.keys())[0]}". Возраст питомца: {list(pets[list(pets.keys())[0]].values())[1]} {age}. Имя владельца: {list(pets[list(pets.keys())[0]].values())[2]}')