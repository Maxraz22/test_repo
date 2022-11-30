class Car(object):
    def __init__(self, brand, color, volume):
        self.brand = brand
        self.color = color
        self.volume = volume

    def forward(self):
        print("Їхати вперед")

    def back(self):
        print("Їхати назад")

my_car = Car("BMW", "Green", "3 liters")

my_car.forward()
my_car.back()

class Car2(Car):
    def __init__(self, brand, color, volume):
        Car.__init__(self, brand, color, volume)

    def left(self):
        print("Повернути ліворуч")

    def right(self):
        print("Повернути праворуч")

my_car2 = Car2("Audi", "Red", "2 liters")

my_car2.left()
my_car2.right()
my_car2.forward()
my_car2.back()
