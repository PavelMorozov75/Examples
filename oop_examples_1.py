
'''
class Base:
    def price(self):
        return 10
class InterFoo(Base):
    def price(self):
        return super().price() * 1.1
class Discount(InterFoo):
    def price(self):
        return super().price() * 0.8
#делаем сначала наценку 10%, потом скидку 20%
print(Discount().price())  #>>>>  8.8
discount = Discount()
print(sorted(discount.__dir__()))
print(sorted(dir(discount)))
print(dir(discount).sort())
'''

'''
class Car:
    pass

car_a = Car()
print(type(car_a))


class Car:
    # создаем атрибуты класса
    car_count = 0

    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

car_a = Car()
car_a.start("Corrola", "Toyota", 2015)
print(car_a.name)
print(car_a.car_count)

car_b = Car()
car_b.start("City", "Honda", 2013)
print(car_b.name)
print(car_b.car_count)
'''

'''
class Square:

    @staticmethod
    def get_squares(a, b):
        return a * a, b * b

    def get_squares_1(self, a, b):
        return a * a, b * b


print(Square.get_squares(3, 5))

g_s = Square()
print(g_s.get_squares(2, 3))
'''

'''
class Point3D:
  x = 10
  y = 10
  z = 10
p1 = Point3D()
p2 = Point3D()
print(p1.x, p1.y, p1.z)
print(p2.x, p2.y, p2.z)
Point3D.x = 20
print(p1.x, p1.y, p1.z)
print(p2.x, p2.y, p2.z)
delattr(Point3D, 'z')
#print(p1.x, p1.y, p1.z)
setattr(p1, 'y', 30)
setattr(Point3D, 'z', 17)
print(p1.x, p1.y)
print(p1.x, p1.y, p1.z)
print(p2.__dict__)

print(hasattr(p2, 'z'))
setattr(p2, 'x', 5)
delattr(p2, 'x')
print(dir(p2))
'''

class Point3D():

    coords = []

    def __init__(self, x=1, y=2, z=3):
        self.x = x
        self.y = y
        self.z = z

    def set_coords(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coords(self):
        return (self.x, self.y, self.z)

class Point(Point3D):
    pass

for _ in range(3):
    x, y, z = map(int, input().split())
    obj = Point(x, y, z)
    Point.coords.append(obj.get_coords())
else:
    print(Point.coords)


