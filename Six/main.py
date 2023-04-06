#5 Задание.

def is_divisible_by_6(number):
    if number % 2 == 0:
        num = number
        sum = 0
        while (num != 0):
            sum += num % 10
            num //= 10
        if sum % 3 == 0:
                print(f'Число {number} делится на 6')
        else:
                print(f'Число {number} неделимо на 6')
    else:
        print(f'Число {number} неделимо на 6')

is_divisible_by_6(6854)

