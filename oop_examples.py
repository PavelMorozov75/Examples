class CC:
    pass

__all__ = [CC]

'''
class Holyday:
    pass

friends = Holyday()
friends.name1 = 'Sveta'
friends.name2 = 'Katya'
friends.name3 = 'Lena'
friends.name4 = 'Natasha'
friends.name5 = 'Pavel'
# Код ниже пожалуйста не удаляйте, ради Машеньки!
#a = friends.__dict__
for i in friends.__dict__:
    if i != 'name5':
        print(getattr(friends, i))
    elif i == 'name5' and getattr(friends, i) == 'Leonid':
        raise AttributeError('Машенька хочет увидеть вас на ДР')
    else:
        pass
'''

'''
class Human:

    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info (self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default_Name: {Human.default_name}')
        print(f'Default_Age: {Human.default_age}')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Not enough money')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money. Current value{self.__money}')

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price - self._price * discount/100
        print(f'Final price: {final_price}')
        return final_price

class SmallHouse(House):
    default_area = 40
    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)



Human.default_info()
alexander = Human('Sacha', 27)
alexander.info()
small_house = SmallHouse(8500)
alexander.buy_house(small_house, 5)
alexander.earn_money(5000)
alexander.buy_house(small_house, 5)
alexander.earn_money(20000)
alexander.buy_house(small_house, 5)
alexander.info()

fedor = Human('Fedor', 25)
fedor.info()
Human.default_info()
fedor.earn_money(10000)
fedor.info()
house = House(100, 15000)
fedor.buy_house(house, 3)
'''



'''
file = {'name': 'Alex', 'age': 18, 'hobby': 'films'}
class Person:
    pass

id_1 = Person()

for key, value in file.items():
    setattr(id_1, key, value)
    # id_1.key = value             # через точку так не получится

print(id_1.hobby)  # films
'''


'''
class Person:
    pass
id_1 = Person()
setattr(id_1, 'name', 'Vasya')
setattr(id_1, 'name', 'Masha')
print(id_1.name)
'''

'''
file = ['name', 'age', 'hobby', 'lolo']

class Person:
    hobby = 'films'

for value in file:
    if getattr(Person, value, False):
        print(value)
'''

'''
class Person:
    hobby = 'dance'
    work = 'design'
    study = 'college'

id_1 = Person()
print(getattr(id_1, 'hobby'))
print(getattr(id_1, 'work'))
print(getattr(id_1, 'study'))
'''

'''
class Pockemon:
    pass
pockemons = Pockemon()

pocks =['pikachu', 'scyther', 'gyarados', 'gengar']
for pock in pocks:
    setattr(pockemons, pock, '')
pocks_for_check = ['lapras', 'pikachu', 'alakazam']
for pock in pocks_for_check:
    print(hasattr(pockemons, pock))
'''

'''
# ваш код: аттрибут класса устанавливаем экземпляру класса
class Person:
    setup = ['set_name', 'set_age', 'set_work', 'set_study']
id_1 = Person()
for i in range(len(id_1.setup)):
    setattr(id_1, id_1.setup[i], input(f"введите {id_1.setup[i][4:]} "))

# код ниже пожалуйста не удаляйте:
for value in id_1.setup:
    print(getattr(id_1, value))
'''


'''
import random
lucky = [random.randint(0, 29), random.randint(0, 29), random.randint(0, 29)]
magic_ing = ["Черные коты", "Лягушачьи глаза", "Паутина", "Корень мандрагоры",
             "Жабий язык", "Женский волос", "Крысы", "Любовное зелье", "Кровь дракона",
             "Пепел отрока","Чертополох", "Пыльца беладонны", "Черная свеча",
             "Сердце ворона", "Собачий клык", "Масло лунного света", "Костыли ведьмы",
             "Подземный гриб","Крыло летучей мыши","Ядовитый плющ", "Перо ворона",
             "Камень чародея", "Слезы совы","Горсть звездной пыли","Волшебный кристалл",
             "Костер из драконьих костей","Зелье бессмертия","Черная роза",
             "Древний свиток заклинаний", "Ключ от врат ада"]

# ниже ваш код:
class Magic:
    pass

setattr(Magic, 'ingredients', [magic_ing[i] for i in lucky]) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
my_coctail = Magic()
for i in range(len(my_coctail.ingredients)):
    print(getattr(my_coctail, 'ingredients')[i])
print("Спасибо, Машенька!")

'''

'''
names = ['Klementina', 'Roza', 'Balu', 'Lena', 'Leonid']  # список имён

class Person:
    Vasya = ''
    Masha = ''
    Lena = ''
    Leonid = ''

# ниже ваш код:
for name in names:
    if hasattr(Person, name):
        delattr(Person, name)
# строки ниже не удаляйте, ради вселенной:
print(len(Person.__dict__))
'''

'''
class Village:

    # ваш метод add_distance
    def add_distance(self, dist):
        # distance = 0
        print(dist - self.distance)

vasya = Village()
masha = Village()
slava = Village()

vasya.distance = 200
masha.distance = 400
slava.distance = 700
vasya.add_distance(1000)
masha.add_distance(1000)
slava.add_distance(1000)
'''



'''
class Person:
    pass
person_1 = Person()
person_1.__dict__ = {'name': 'Vasya', 'age': '20', 'work': 'driver'}
for key in person_1.__dict__:
    print(person_1.__dict__[key])
'''

'''
class CountDistanse:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def dist_count(start, finish):
        dist = ((finish.x - start.x) ** 2 + (finish.y - start.y) ** 2) ** 0.5
        print(round(dist))

class Point(CountDistanse):
    pass

p1 = Point(10, 20)
p2 = Point(20, 30)

CountDistanse.dist_count(p1, p2)
'''

'''
class Dog():
    tail = 1
    paws = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print('ГавГав')

class Human():
    def __init__(self, name):
        self.name = name

    def adopt_dog(self, dog):
        self.my_dog = dog

    def print_human_name(self):
        print(self.name)

    def print_dog_name(self):
        print(self.my_dog.name)




dog = Dog('Шарик', 'черный')
human = Human('Вася')
human.adopt_dog(dog)
human.print_dog_name()
human.my_dog.bark()       # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
human.print_human_name()
'''

'''
class EvenLenghtMixin:
    # a = 6
    def even_lenght(self):
        # self.b = 8
        return len(self) % 2 == 0

class Mylist(list, EvenLenghtMixin):
   def pop(self):
       x = super(Mylist, self).pop()
       # x = super().pop
       print('last_value', x)
       return x

print(Mylist.mro())
x = Mylist()
x.extend([1, 2, 3, 4, 5])
print(x.even_lenght())
x.append(6)
print(x.even_lenght())
x.pop()
print('действительно родитель  ', issubclass(Mylist, EvenLenghtMixin))
print('действительно родитель  ', issubclass(EvenLenghtMixin, object))
print('Дейстрвительно экземпляр класса', isinstance(x, Mylist))
print(Mylist.__dict__)
print(x.__dict__)
'''

'''
from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
'''


'''
class Minecraft:
    def hello_creeper(self):
        print("Hello, Creeper")

class Roblox(Minecraft):
    def hello_all(self):
        super().hello_creeper()
        print('Hello, Pozzy')
hello = Roblox()
hello.hello_all()
'''

'''
class Alfa:
    @staticmethod
    def sum_number(x, y):
        return x + y

class Beta(Alfa):
    def result(self, x, y , z):
        summa = super().sum_number(x,y)
        print(summa/z)
test = Beta()
test.result(10, 20, 30)
'''

'''
class A:
    def __init__(self):
        print('класс А')
        super().__init__()



class B:
    def __init__(self):
        print('класс В')


class C:
    def __init__(self):
        print('класс С')


class D(A, B, C):
    pass

d = D()
'''

'''
class User:
    def __init__(self, name):
        self.name = name

        # создайте метод __getattribute__

    def __getattribute__(self, item):
        return f"{object.__getattribute__(self, item)}man"


user1 = User("Super")
user2 = User("Bat")
user3 = User("Spider")

print(user1.name, user2.name, user3.name, sep='\n')
'''


'''
class Person:
    def __getattr__(self, name):
        if name == 'name':
            return 'Vasya'
        else:
            return 'Такого атрибута нет'
person = Person()
print(person.name)
'''

'''
class OnlyVasya:
    def __setattr__(self, name, value):
        if name == 'name':
            value = 'Vasya'
        return super().__setattr__(name, value)
obj = OnlyVasya()
obj.name = 'Masha'
print(obj.name)
'''
'''
class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.s = self.a + self.b
        del self.s

    def __delattr__(self, name):
        if self.s > 10:
            pass
        else:
            super().__delattr__(name)

number1 = Number(4, 5)
print('s' in number1.__dict__)

number2 = Number(6, 11)
print('s' in number2.__dict__)
'''

'''
class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __delattr__(self, name):
        if name == 'a':
            print('не буду удалять a')
            pass
        else:
            super().__delattr__(name)

num = Number(b=4,a=7)
del num.a
del num.b
print(num.a)
'''

'''
class Cord:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if isinstance(other, Cord):     # принадлежит ли экземпляр классу Cord?
            return self.x == other.x
        if isinstance(other, int):      # принадлежит ли экземпляр классу int?
            return self.x == other
        if isinstance(other, Cord1):
            return self.x == other.x

    def __ne__(self, other):
        return not self.__eq__(other)

class  Cord1:
    def __init__(self,x):
        self.x = x


cord1 = Cord(50)
cord2 = Cord(50)
cord11 = Cord1(25)

print(cord1 == cord2)  # True
print(cord1 == 50)     # True

print(cord1 != cord2)  # False
print(cord1 != 50)     # False
print(cord1 == cord11) # False
'''



'''
class Words:
    def __init__(self, word):
        self.word = word

    def __eq__(self, other):
        return len(self.word) == len(other.word)

word_1 = Words('Vasya')
word_2 = Words('Masha')
print(word_1 == word_2)
'''

'''
class Number:
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        if isinstance(other, Number):
            return self.number + other.number
        if isinstance(other, int):
            return self.number + other

num1 = Number(100)
num2 = Number(200)
print(num1 + num2)
print(num1 + 300)
print(num2 + 300)
'''

'''
class Number:
    def __init__(self, number):
        self.number = number

    def __isub__(self, other):
        if isinstance(other, Number):
            self.number -= other.number  # экземпляр вычитает экземпляр
            return self
        if isinstance(other, int):
            self.number -= other         # экземпляр вычитает число
            return self

num1 = Number(50)
num2 = Number(20)

num1 -= num2
print(num1.number)  # 30
num1 -= 30
print(num1.number)  # 0
'''

'''
class Number:
    def __init__(self, x):
        self.x = x
    def __sub__(self, other):
        if isinstance(other, Number):
            return self.x - other.x

num1 = Number(70)
num2 = Number(20)
print(num1-num2)
'''

'''
class Hello:
    def __init__(self, say):
        self.say = say

    # Ваш код
    def __mul__(self, other):
        if isinstance(other, int):
            return self.say * other

lang = Hello('Hello!')
print(lang * 3)  # Hello!Hello!Hello!
'''

'''
class Number:
    def __init__(self, number):
        self.number = number

    def __pow__(self, power):
        if isinstance(power, int):
            return self.number ** power
num = Number(10)
print(num**2)
'''

'''
class Number:
    def __init__(self, number):
        self.number = number

    def __truediv__(self, other):
        if isinstance(other, int) and other != 0:
            return self.number / other
        if other == 0:
            return 'на ноль делить нельзя'

num = Number(10)
print(num / 2 )
print(num / 0)
'''
'''
class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        if isinstance(other, Number):
            result = self.number + other.number
        else:
            result = self.number + other
        return Number(result)  # создаёт новый экземпляр

    def __radd__(self, other):
        result = self.number + other
        return Number(result)  # создаёт новый экземпляр

obj1 = Number(10)
obj2 = Number(20)
obj3 = obj1 + 5 + obj2

print(obj3.number) # 35
'''


'''
class Number:
# Объявите здесь все необходимые методы для операций
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        if isinstance(other, int):
            return self.number + other
    def __truediv__(self, other):
        if isinstance(other, int) and other != 0:
            return self.number / other
    def __mul__(self, other):
        if isinstance(other, int):
            return self.number * other
    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            return self.number ** power

    def __sub__(self, other):
        if isinstance(other, int):
            return self.number - other

    def __abs__(self):
        return abs(self.number)

# код ниже не меняйте ради вселенной
num1 = Number(-10)
result1 = num1 + 90
result2 = num1 / 10
result3 = num1 * -1
result4 = num1 ** 2
result5 = num1 - 20
result6 = abs(num1)
print(result1, result2, result3, result4, result5, result6)
'''

'''
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Да здравствует {self.name}!"
        # напишите ваш код

# Код ниже пожалуйста не меняйте:
input_word = input()
person = Person(input_word)
print(person)
'''

'''
class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color  = color
        self.year = year

    def __str__(self):
        return f"{self.__class__.__name__}"  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!

car = Car('toyota corolla', 'black', 2023)
print(f"Класс: {car},", f"Атрибуты экземпляра: {car.__dict__}")
'''

'''
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    # ваш код:
    def __hash__(self):
        return hash((self.model, self.color)) # внимание скобки !!!!




car1 = Car("toyota corolla", "black")
car2 = Car("toyota corolla", "black")
print(hash(car1) == hash(car2))
'''

'''
class MyPhone:
    def __init__(self):
        self.phone = ['Nokia', 'Iphone', 'Samsung', 'Huawei', 'LG']

    def __str__(self):
        return str(self.phone)

    # напишите ваши методы
    def __setitem__(self, key, value):
        self.phone[key] = value

    def __delitem__(self, key):
        del self.phone[key]

    def __getitem__(self, item):
        return self.phone[item]

    def kruchu_verchu(self, value):
        self.phone.append(value)


# код ниже не меняйте, но присмотритесь
my_phone = MyPhone()

my_phone[1] = 'Xiaomi'
del my_phone[2]
my_phone.kruchu_verchu('HONOR')

print(my_phone)
print(my_phone[4])
'''

'''
class Present:
    def __init__(self):
        self.present = ['book', 'Iphone', 'TV', 'snowman', 'car']

    # ваши методы

    def __getitem__(self, item):
        return self.present[item]

    def __len__(self):
        return len(self.present)

    def __delitem__(self, key):
        del self.present[key]

holiday = Present()
# ваш код, если потребуется
del holiday[-1]

# код ниже не удаляйте, ради Маши!
if len(holiday) == 4:
    print(holiday[3])

'''

'''
class Country:
    country = ('Russia', 'Ukraine', 'Belarus', 'Kazakhstan', 'Other')

    # создайте метод(ы)
    def __getitem__(self, item):
        return Country.country[item]


# код ниже, не меняйте, ради Машеньки
country_is = Country()
for i in country_is:
    if i == 'Kazakhstan':
        print(f'Ура, Маша летит в Казахстан!')
'''


'''
class Options:
    def __init__(self):
        self.attr1 = "value1"
        self.attr2 = "value2"

options = Options()
options_dict = vars(options)

print(options_dict) # Output: {'attr1': 'value1', 'attr2': 'value2'}
print(options.__dict__)
print(Options.__dict__)
'''


class GuruPython:


    '''Это документация класса GuruPython'''
    def __init__(self, a, b):
        '''Это конструктор класса GuruPython'''
        self.a = a
        self.b = b

    def return_ab(self):
        '''Это метод класса GuruPython'''
        return self.a + self.b
# print(GuruPython.__doc__)
# print(GuruPython.__init__.__doc__)
# print(GuruPython.return_ab.__doc__)

'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

account = BankAccount(1500)
print(account.__dict__)               # {'_BankAccount__balance': 1500}
print(account._BankAccount__balance)  # 1500
'''

'''
class Parent:

    def __init__(self, y, a):
        self.__y = y
        self._a = a

    def __parent_y(self):
        print(self.__y)

    def _pparent(self):
        print(self._a)

class Child(Parent):
    def child__x(self):
        print(self.__y)


coordinate = Parent(5, 17)    # экземпляр дочернего класса
print(coordinate.__dict__)

coordinate._pparent()
#coordinate.__parent_y() # невозможно вызвать приватный метод
print(coordinate._Parent__y)  #
'''

'''
class Bank:
    def __init__(self, name, number, balance):
        self._name = name
        self._number = number
        self._balance = balance

    def print_balance(self):
        print(self._balance)

    def change_balance(self, money):
        self._balance = self._balance + money

id_1 = Bank('Vasya', 12345678, 1000)
id_1.change_balance(-500)
print(id_1.__dict__)
id_1.print_balance()
'''

'''
from accessify import private

class MyClass:
    a = 2
    b = 3

    @private
    def private_sum_ab(self):
        print(f"{self.a + self.b}")

    def public_sum_ab(self):
        self.private_sum_ab()

obj = MyClass()
obj.public_sum_ab()   # 5 - приватный метод можно вызвать из публичного
# obj.private_sum_ab()  # AttributeError
'''

'''
from accessify import private
class Teleport:

    @private
    def __activator_teleport(self):
        print("Активатор от телепорта у Машеньки под подушкой")

    def mama_help(self):
        self.__activator_teleport()

vasya = Teleport()
vasya.mama_help()

class MagicBank:
    def __init__(self, account, balance):
        self.__account = account
        self.__balance = balance

    # ваши методы
    @property
    def happy_balance(self):
        return self.__balance
    @happy_balance.setter
    def happy_balance(self, balance):
        self.__balance = balance

    @happy_balance.deleter
    def happy_balance(self):
        self.__balance = 0



# Код проверки пожалуйста не удаляйте

id_1 = MagicBank('Машенька', 500)
print(id_1.happy_balance)

id_1.happy_balance = 1000
print(id_1.happy_balance)

del id_1.happy_balance
print(id_1.happy_balance)
'''


'''
class Person:
    message_counter = 0
    # объявите ваш метод

    def print_number_of_messages(self):
        print(self.message_counter)

id_1 = Person()
id_2 = Person()

id_1.message_counter = 5
id_2.message_counter = 10

# ваш код вызова метода:
id_1.print_number_of_messages()
id_2.print_number_of_messages()
'''



'''
class MyClass:
    name = "Hello"

    @classmethod
    def set_attr(cls, new_name):
        cls.name = new_name

    @classmethod
    def get_attr(cls):
        print(cls.name)


MyClass.get_attr()  # выводит значение атрибута name, то есть "Hello"

MyClass.set_attr("Vasya")  # Переименовал атрибут name в классе на значение "Vasya"
print(MyClass.name)  # Vasya
'''

'''
class NewJournal:

    def set_attr(self, papa, mama, deda, baba):
        self.papa = papa
        self.mama = mama
        self.deda = deda
        self.baba = baba
        self.count_money = self.papa + self.mama + self.deda + self.baba

    def check_money(self):
        if self.count_money < 80:
            print('Денег не хватает')
        else:
            print('Ура, денег хватает!')

masha = NewJournal()
masha.set_attr(10, 20, 30, 40)
masha.check_money()
'''

'''
class GPS:
    distance1 = ("Москва", "Екатеринбург", 1860)
    distance2 = ("Москва", "Казань", 840)
    distance3 = ("Москва", "Нижний Новгород", 430)

    # ваш метод
    def count_distance(self, point1, point2):
        if point1 == point2:
            print(0)
        else:
            for route in [self.distance1, self.distance2, self.distance3]:
                if (point1 in route) and (point2 in route):
                    print(route[2])
                    break
            else:
                print("Извините, программа ещё в разработке")
#Напомню, else в цикле выполняется всегда в конце всех итераций, если в цикле не активировался break!!!!!!
# код ниже пожалуйста не удаляйте
dis1 = GPS()
dis2 = GPS()
dis3 = GPS()

dis1.count_distance("Москва", "Казань")
dis2.count_distance("Екатеринбург", "Москва")
dis2.count_distance("Казань", "Казань")
dis3.count_distance("Нижний Новгород", "Екатеринбург")
'''




