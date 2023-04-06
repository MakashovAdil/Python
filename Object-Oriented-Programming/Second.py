#2.

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        print(f"Вместимость одного автобуса {self.name}: {capacity} пассажиров")

class Autobus(Transport):
    capacity = 50
    def seating_capacity(self, capacity):
        self.capacity = capacity
        print(f"Вместимость одного автобуса {self.name}: {capacity} пассажиров")


auto = Autobus("Renaul Logan", 180, 12)
auto.seating_capacity(Autobus.capacity)
