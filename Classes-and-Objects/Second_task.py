#2 Задание.

class Turtle:

    def __init__(self, x, y, s):
        self.position_x = x
        self.position_y = y
        self.cells = s

    def go_up(self):
        self.position_y += self.cells

    def go_down(self):
        self.position_y -= self.cells

    def go_left(self):
        self.position_x -= self.cells

    def go_right(self):
        self.position_x += self.cells 

    def evolve(self):
        self.cells += 1

    def degrade(self):
        if self.cells <= 0:
            print("s не может быть меньше нуля")
        else:
            self.cells -= 1

    def count_moves(self, x2, y2):
        steps = 0
        while self.position_x != x2:
            if x2 < 0:
                self.position_x -= self.cells
                steps += self.cells
            elif x2 > 0:
                self.position_x += self.cells
                steps += self.cells
            else: 
                self.position_x == self.position_x

        while self.position_y != y2:
            if y2 < 0:
                self.position_y -= self.cells
                steps += self.cells
            elif y2 > 0:
                self.position_y += self.cells
                steps += self.cells
            else: 
                self.position_y == self.position_y

        print(steps)

t = Turtle(0, 0, 1)
t.count_moves(5,5)




