class Person:

    message_counter = 13

    dict_all = {'name': 'Vasya', 'age': 15}

    @classmethod
    def print_number_of_messages(cls):
        print('@classmethod cls.message_counter до:', cls.message_counter)
        cls.message_counter -= 1
        print('@classmethod cls.message_counter после:', cls.message_counter)


    def print_static(cls):
        cls.print_number_of_messages()


    def print_number_of_messages_1(self):
        print('\n', 'вызов обычного метода')
        print('message_counter', self.message_counter) # через self можно обратиться к переменной класса
        self.message_counter = self.message_counter + 2 # в экземпляре
        Person.message_counter = Person.message_counter + 1 # в классе, меняем у всех экземпляров
        print('message_counter', self.message_counter)# через self можно обратиться к переменной класса
        print('Person.message_counter  ', Person.message_counter)
        print('message_counter', self.message_counter)
        # Person.print_number_messages()#classmethod в методе так не прокатывает в обычном методе
        # cls.print_number_messages()  # classmethod в методе так не прокатывает
        self.print_number_messages_2()#staticmethod
        Person.print_number_messages_2()#staticmethod
        self.print_number_of_messages()

    @staticmethod
    def print_number_messages_2():
        print(25)

id_1 = Person()

#id_1.message_counter = 5
id_2 = Person()
print('id_2.message_counter :', id_2.message_counter)#13 !!!!


id_1.print_static()
Person.print_number_of_messages()# вызов метода класса через класс
id_1.print_number_of_messages()#вызов метода класса через экземпляр
id_1.print_number_of_messages_1()#вызов обычного метода
Person.message_counter = 77

print('id_1.message_counter  :', id_1.message_counter)
id_1.print_number_messages_2()# вызов статического метода через экземпляр
print(id_1.__dict__)
print(id_2.__dict__)

print('id_1.message_counter  :', id_1.message_counter)

#print(id_1.name) не срабатывает, аттрибута name нет !!!!!
id_1.__dict__ = Person.dict_all



print('id_1.name :', id_1.name)#Vasya - теперь срабатывает!!!
id_1.name = 'Sonja'
id_2.__dict__ = Person.dict_all

print('id_1.age :', id_1.age) #15
print('id_2.name', id_2.name)# 'Sonja' !!!!!!!!!!!!!! а не Vasya !!!!!!!!!!!
print('id_1.message_counter  :', id_1.message_counter)#хоть и присвоили экземпляру новый dict аттрибут message_counter остался !!!
print(Person.dict_all) #{'name': 'Sonja', 'age': 15}
'''
class Person:
    @classmethod
    def create_person(cls, name, age):
        person = cls()
        person.name = name
        person.age = age
        return person

person1 = Person.create_person("Vasya", 25)
print(person1.name)  # Vasya
print(person1.age)   # 25
'''

'''
class Time:
    @staticmethod
    def count_time(distance, speed):
        return distance / speed


print(Time.count_time(500, 100))
'''

'''
class Example:
    @classmethod
    def method_for_class(cls, x,y):
        cls.x = x
        cls.y = y
        print(cls.x*cls.y)
Example.method_for_class(5,20)
'''

'''
class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        date1 = cls(day, month, year)
        return date1

    def string_to_db(self):
        return f'{self.year}-{self.month}-{self.day}'

date1 = Date.from_string('30.12.2020')
date1.string_to_db()
# '2020-12-30'
date2 = Date.from_string('01.01.2021')
date2.string_to_db()
# '2021-1-1'
'''


'''
# ваш код:
class Counter:

    count = 0
    @classmethod
    def add_count(cls, add=1):
        cls.count += add
    @classmethod
    def set_zero(cls):
        cls.count = 0

# код ниже пожалуйста не удаляйте
Counter.add_count()
print(Counter.count)
Counter.set_zero()
print(Counter.count)
Counter.add_count(110)
Counter.add_count()
print(Counter.count)
'''

'''
# ваш код:
class MagicBank:
    money = 1000

    @classmethod
    def add_money(cls):
        cls.money = 1000
        print('Ваш счёт снова равен 1000', end='\n\n')#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    @classmethod
    def reduce_money(cls, amount):
        if amount > 1000:
            print('Нельзя тратить больше 1000 за один раз')
        else:
            print(f'Покупка на сумму {amount} осуществлена')
            cls.add_money()

# код ниже пожалуйста не удаляйте
masha = MagicBank()
masha.reduce_money(100)   #вызвали через экземпляр метод класса !!!!!!!!!!!!!!!!
masha.reduce_money(999)
masha.reduce_money(1000000000)
'''

'''
class Driver:
    @staticmethod
    def calculate_fuel_costs(distance, fuel, price):
        result = price * distance * fuel / 100
        print(round(result, 2))
        return result

vasya = Driver()
vasya.calculate_fuel_costs(3, 7, 50)
vasya.calculate_fuel_costs(100, 7, 50)
vasya.calculate_fuel_costs(50, 7, 50)
'''
'''
from datetime import datetime

# ваш код:
class Product:
    @staticmethod
    def check_date(today, expiry):
        start = datetime.strptime(today, "%Y-%m-%d")
        finish = datetime.strptime(expiry, "%Y-%m-%d")

        print('Срок годности в порядке' if finish > start else 'Срок годности истёк')# !!!!!!!!!!!!!!

        # if finish > start:
        #     print('Срок годности в порядке')
        # else:
        #     print("Срок годности истёк")



# код ниже пожалуйста не удаляйте
today_date = "2024-01-12"
expiry_date1 = "2024-01-31"
expiry_date2 = "2024-01-1"
expiry_date3 = "2024-01-12"

Product.check_date(today_date, expiry_date1)
Product.check_date(today_date, expiry_date2)
Product.check_date(today_date, expiry_date3)
'''
class MyClass:
    class_attribute = "Hello"

    @classmethod
    def say_hello(cls):
        print(cls.class_attribute)

MyClass.say_hello()         # Выводит "Hello"

my = MyClass()
my.class_attribute = "hi"   # Создали атрибут class_attribute в экземпляре my

my.say_hello()              # Выводит всё равно "Hello"
MyClass.class_attribute = 'hihi'
my.say_hello()# Выводит 'hihi'
print(my.class_attribute)# Выводит 'hi'
my1 = MyClass()
print(my1.class_attribute)# Выводит 'hihi'


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

