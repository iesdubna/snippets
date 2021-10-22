from math import sqrt

class Figure:
    def __init__(self):
        self.painted = False
        self.color = "Unknown"

    def paint(self, color):
        self.painted = True
        self.color = color    

    def area(self):
        print("I don't know how to calculate area")


class Circle(Figure):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class Triangle(Figure):
    def __init__(self, a=None, b=None, c=None, d=None, h=None):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h
        if (a is None or b is None or c is None) and (d is None or h is None):
            raise Exception("Triangle is not properly defined")
    
    def area(self):
        if self.a is not None and self.b is not None and self.c is not None:
            s = (self.a + self.b + self.c)/2.0 
            return sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        else:
            return self.d * self.h / 2.0
        

t = Triangle(a=3, b=4, c=5)
t2 = Triangle(d=3, h=4)

print(t.area())
print(t2.area())
