class Parallelogram(object):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        s1 = self.width * self.length
        return s1

s1 = Parallelogram(5, 10)
print(s1.get_area())

class Square(Parallelogram):
    def __init__(self, width, length):
        Parallelogram.__init__(self, width, length)

    def get_area(self):
        if self.width == self.length:
            s2 = self.width ** 2
        else:
            s2 = self.width * self.length
            print("Це не квадрат!")
        return s2

s2 = Square(5, 5)
print(s2.get_area())
