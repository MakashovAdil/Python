#4 Задание.

#def is_alive(health):
#    if:
#        health < 0
#        False
#    else:
#        return true
 
def is_alive(health):
    if health > 0:
        print(True)
    else:
        print(False)

is_alive(int(input("Сколько у вас здоровье? -> ")))
