from abc import ABCMeta, abstractmethod


class Point():
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y


class Line():
    def __init__(self, x, y):
        self.line = Point(x,y)

    def length(self):
        return print(f'Длина линии - {self.line.y - self.line.x}')


x = Line(5.0, 9.4)
x.length()


class Shape():
    __metaclass__=ABCMeta

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass


class Square(Line,Shape):
    def __init__(self, x, y):
        Line.__init__(self, x, y)

    @property
    def area(self):
        area = (self.line.y - self.line.x) ** 2
        return area
    
    @property
    def perimeter(self):
        perimeter = (self.line.y - self.line.x) * 4
        return perimeter

x1 = Square(2.0, 6.2)
print(f'Площадь квадрата - {x1.area}')
print(f'Периметр квадрата - {x1.perimeter}')


class Rect(Shape):
    def __init__(self, w, h):
        self.points = Point(w,h)

    @property
    def area(self):
        return float(self.points.x * self.points.y)
    
    @property
    def perimeter(self):
        return float(2 * (self.points.x + self.points.y))


x2 = Rect(1,4)
print(f'Периметр прямоугольника - {x2.perimeter}')
print(f'Площадь прямоугольника - {x2.area}')


class Cube(Square):
    def __init__(self, x, y = None):
        Square.__init__(self, x, y)
    
    @property
    def area(self):
        return (6 * (self.line.x**2))

    @property
    def perimeter(self):
        return (12*self.line.x)
    
    def volume(self):
        return (self.line.x**3)

cube1 = Cube(5)
print(f'Периметр куба равен - {cube1.perimeter}')
print(f'Площадь куба равна - {cube1.area}')
print(f'Объём куба равен - {cube1.volume()}')
