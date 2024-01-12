
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
# ваш код:
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