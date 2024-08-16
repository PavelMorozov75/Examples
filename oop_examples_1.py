
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

        def __init__(self, x=4, y=5,z=7):
            self.x = x
            self.y = y
            self.z = z

            super().__init__(self.x, self.y, self.z)

for _ in range(3):
    x, y, z = map(int, input().split())
    obj = Point(x, y, z)
    Point.coords.append(obj.get_coords())
else:
    print(Point.coords)
'''

'''
class Word(str):
    

    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print ("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] # Теперь Word это все символы до первого пробела
        return str.__new__(cls, word)

ww = Word('yyyy iii')
print(ww)
'''

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')
class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):

    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):

    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):

    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


salary_employee = SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])

