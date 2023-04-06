#1 Задание. 

class Cash:

    def __init__(self, money):
        self.money = money

    def top_up(self, X):
        self.money += X
        print(self.money)

    def take_away(self, X):
       if self.money >= X:
           self.money -= X
           print(self.money)
       else:
           print("Недостаточно средств")

    def count_1000(self):
        x = self.money // 1000
        print(x)

a = Cash(3500)
a.top_up(1000)
a.take_away(500)
a.count_1000()