
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
class Person:
    pass

person_1 = Person()
person_1.__dict__ = {'name': 'Vasya', 'age': '20', 'work': 'driver'}
for key in person_1.__dict__:
    print(person_1.__dict__[key])
