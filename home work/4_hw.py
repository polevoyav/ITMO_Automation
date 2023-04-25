print('Первое задание')

class Rectangle:

    def __init__(self, dln, shir):
        self.gln = dln
        self.shir = shir
    def prmtr(self):
        return (self.gln + self.shir)*2
    def area(self):
        return self.gln * self.shir

rct = Rectangle (10, 10)
rct.prmtr()
rct.area()
print('Периметр: ', rct.prmtr())
print('Площадь: ',rct.area())
print()

print('Второе задание')
class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def slogr(self):
        return self.a + self.b
    def vuch(self):
        return self.a - self.b
    def umn(self):
        return self.a * self.b
    def dele(self):
        return self.a - self.b
ab = Math(10, 10)
ab.slogr()
ab.vuch()
ab.umn()
ab.dele()
print('сложение: ', ab.slogr())
print('вычитание: ', ab.vuch())
print('умножение: ', ab.umn())
print('деление: ', ab.dele())
print()
