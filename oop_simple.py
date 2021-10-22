# encapsulation, polymorphism, inhertence

class A:
    def __init__(self, a, b):
        self.first = a
        self.second = b

    def sum(self):
        return self.first + self.second


class B(A):
    def diff(self):
        return self.first - self.second



x = A(1, 2)
y = A(3, 4)
z = B(5, 6)
print(x.sum())
print(y.sum())
print(z.sum())
print(z.diff())
