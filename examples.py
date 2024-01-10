'''
fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31))

f = lambda x : 1 if x < 2 else x*f(x-1)
print(f(5))

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(map(lambda x: x*2 , current_list))
print(new_list)
'''

'''
count = int(input('введите количество чисел   '))
summa = 0
for i in range(1, count + 1):
    summa = summa + int(input('введите слагаемое  '))
print(summa)
'''

'''
x = [1, 2, 3]
print(type(id(x)))
y = x
print(id(y))
print(y is x)
print(y is [1, 2, 3])

x.append(4)
print(x, y)
'''

'''
x = [1, 2, 3]
y = x
y.append(4)
print(type(x))
s = "123"
t = s
t = t + "4"
print(str(x) + " " + s)
'''


'''
x = 4
y = 4
print (x is y)
'''
'''
objects = [1,1,2,'a',23,23,4,45,15,1,1,1,1]
new_objects = []

i = 0
for obj in objects: # доступная переменная objects
    count = objects.pop(i)
    if obj not in objects:
        new_objects.append(count)
    else:
        for j in objects:
            if count == j:
                objects.remove(j)
    i+= 1


print(len(new_objects))
#print(ans)
'''
'''
objects = [1,1,2,'a',23,23,4,45,15,1,1,1,1]
new_objects = []
for i in range(0, len(objects)+1):
    count = objects.pop(i)
    if count not in objects:
        new_objects.append(count)
    else:
        for j in range(0, len(objects)+1):
            if count == objects[j]:
                objects.pop(j)

print(len(new_objects))
'''

'''
objects = [1,1,2,'a',23,23,4,45,15,1,1,1,1,'a',12,33]
count = []
for obj in objects: # доступная переменная objects
    i = 0
    for j in objects:
        if obj is j:
            i+=1
    count.append(i)
print(count)
ans =0
for j in count:
    if j == 1:
        ans +=1
print(ans)
'''


'''
def closest_mod_5(x):
    i = 0
    while (x+i) % 5 != 0:
        i+=1
    return x+i

print(closest_mod_5(21))
'''



'''
def C(n, k):
    if k ==0:
        return 1
    elif k > n:
        return 0
    else:
        return (C(n-1, k) + C(n-1, k-1))


n, k = map(int, input().split())
print(C(n, k))
'''

'''
ok_status = True
vowles = ['a', 'e', 'u', 'i', 'o']


def check_word(word):
    #global ok_status
    for i in vowles:
        if i in word:
            return True

    ok_status = False
    return False


print(check_word('adace'))
print(ok_status)
print(check_word('www'))
print(ok_status)

'''

'''
ok_status = True
vowles = ['a', 'e', 'u', 'i', 'o']
def f():

    ok_status = True
    vowles = ['a', 'e', 'u', 'i', 'o']

    def check_word(word):
        #global ok_status
        nonlocal ok_status
        for i in vowles:
            if i in word:
                return True

        ok_status = False
        return False
    print(check_word('adace'))
    print(ok_status)
    print(check_word('www'))
    print(ok_status)

f()
print(ok_status)
'''


'''
x, y = 1, 2
#print(x)
#print(y)
def foo():
    global y
    if y == 2:
        x = 2
        print(x)
        y = 1

foo()
print(x)
if y == 1:
    x = 3
print(x)
'''

'''
x = 1
def foo():
    #global x
    x = 2
    print(x)
foo()
print(x)
'''

'''
lst = list()
lst = []
'''


'''
class EvenLenghtMixin:
    a = 6
    def even_lenght(self):
        self.b = 8
        return len(self) % 2 == 0

class Mylist(list, EvenLenghtMixin):
   def pop(self):
       x = super(Mylist, self).pop()
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


print('действительно родитель  ', issubclass(Human, object))
print('Дейстрвительно экземпляр класса', isinstance(human, Human))
'''


'''
class Base:
    def __init__(self):
        self.val = 0

    def add_one(self):
        self.val += 1

    def add_many(self, x):
        for i in range(x):
            self.add_one()

class Derived(Base):
    def add_one(self):
        self.val += 10


a = Derived()
a.add_one()

b = Derived()
b.add_many(3)

print(a.val)
print(b.val)
'''


'''
x = [1, 2, 'ddd', 24, 12, 7]
try:
    x.sort()
except TypeError:
    print('TypeError (:')


def f (x, y):
    try:
        return x/y
    except TypeError:
        print('TypeError ((')
    except ZeroDivisionError:
        print('Zerodevizion')

f(10, 0)
'''

'''
def f (x, y):
    try:
        return x/y
    except TypeError:
        print('TypeError ((')
    except ZeroDivisionError:
            print('Zerodevizion')
try:
    f(10, 0)
except ZeroDivisionError:
        print('Zerodevizion')
'''

'''
def f (x, y):
    try:
        return x/y
    except (TypeError, ZeroDivisionError) as e:
        print('Error')
        print(e)
        print(type(e))
        print(e.args)

f(5, 0)
'''

'''
def f (x, y):
    try:
        return x/y
    except: # все исключения
        print('Error')
        print(e)
        print(type(e))
        print(e.args)

f(5, 0)

print(ZeroDivisionError.mro())
'''


'''
def f (x, y):
    try:
        result =  x/y
    except ZeroDivisionError:
        print('ZEROError')
    else: # если ошибки нет
        print(result)
    finally:
        print('finally') # в любом случае


f(5, 0)
f(5, 2)
'''

'''
class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return 'hallo' + name
    else:
        raise BadName(name + ' is inappropriate name')
while True:
    try:
        name = input('Please enter you name ')
        greeting = greet(name)
        print(greeting)
    except BadName:
        print('Try again')
    else:
        break
'''
'''
class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonePositiveError

class NonPositiveError(Exception):
    pass


a = PositiveList()
a.append(3)
print(a)
a.append(-8)

'''

'''
print(__name__)
'''

'''
import sys
sys.path.insert(1, './pages')
import main # Исполним код в файле main в текущей директории
print(sys.modules)
print(type(sys))
for path in sys.path:
    print(path)
'''

'''
import datetime as dt
j, m, d = map(int, input().split())
int_delta= int(input())
new_date = dt.datetime(j,m,d)+dt.timedelta(days=int_delta)
print (int(new_date.strftime('%Y')), int(new_date.strftime('%m')), int((new_date.strftime('%d'))))
print(j, m, d)
print(int_delta)
'''

'''
_CONST = 2 # такие константы, начинающиеся с нижнего подчеркивания нельзя импортировать в другой модуль
__all__ = [ 'greet', 'NonPositiveError'] # эти функция и класс можно будет импортировать в другой модуль
# где будет указано from ... import *, другие функции и классы текущего модуля при этом будет импортировать нельзя
'''
'''
lst = [1, 2, 3, 34]
book = {'author': 'Pushkin', 'title': 'Golden Fish', 'year': 1785}
str = 'Hallo for all'

for i in lst:
    print(i)
for i in book:
    print(i)

iterator = iter(lst)
a = next(iterator)
b = 1 + next(iterator)
print(a)
print(b)
'''

'''
from random import random
class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0
    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration
    def __iter__(self):
        return self

x = RandomIterator(3)
#print(next(x))
#print(next(x))
#print(next(x))
for i in x:
    print(i)
'''


'''
class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return [self.lst[self.i -2], self.lst[self.i -1]]
        else:
            raise StopIteration

class Mylist(list):
    def __iter__(self):
        return(DoubleElementListIterator(self))


for pair in Mylist([1,2,2,4]):
    print((pair))
'''

'''
from random import random
def random_generator(k):
    for i in range(k):
        for j in ['a', 'b']:
            yield {j: random()}

gen = random_generator(2)
#print(next(gen))
#print(next(gen))
#print(next(gen))
print(gen)
for i in gen:
    print(i)
'''

'''
variable = [i*i for i in range(10) if i > 5]
print(variable)

z = [(x, y) for x in range(3) for y in range(3) if x > y]
print(z)

ddict = {'a': 3, 'd': 8, 'c': 1, 'u': 14}
variable = {key: value for key, value in ddict.items() if value > 5}
print(variable)
del variable['d']
print(variable)
'''

'''
a = [i for i in range(5)][1:]
print(a)
'''

'''
def brand_new_iterator():
    i = 0
    while True:
        yield i
        i += 2
        yield i
        i += 1

list1 = []
itrtr = brand_new_iterator()
for i in range(10):
    list1.append(next(itrtr))
print(list1)
'''


# r (read) - открыть для чтения (по умолчанию)
# w (write) - открыть для записи, содержимое файла стирается
# a (append) - открыть для записи, запись ведется в конец
'''
f = open("test.txt")
#d = f.read()
d = f.readline().rstrip()
print(d)
d = f.readline().rstrip()
print(d)
'''
#d = d.splitlines()
#print(d)

'''
for line in f:
    line = line.rstrip()
    print(repr(line))
x = f.read(5)
print(repr(x)) 

f.close()
'''

'''
f = open("test1.txt", "w") # в случае отсутствия файл создастся
lines = ["Line 1", "Line 2", "Line 3"]
contents = "\n".join(lines)
f.write(contents)
f.close()

f = open("test_append.txt", "a")
f.write("Hello\n")
f.close()

with open("test.txt") as f, open("test_copy.txt", "w") as w:
    for line in f:
        w.write(line)
        
'''

'''
f1 = open('test.txt', 'r')
f2  = open('test_new.txt', 'w')
lst = []
#a  = [line.rstrip() for line in f1]
#print(a)

for line in f1:
    lst.append(line.rstrip())
lst.reverse()
count = 1
for i in lst:
    if count  < len(lst):
        f2.write(i+'\n')
        count +=1
    else:
        f2.write(i)


f1.close()
f2.close()
'''

'''
f1 = open('test.txt', 'r')
f2  = open('test_new.txt', 'w')
lst2 = []
while True:
    stro = f1.readline().rstrip()
    if stro == '': # при окончании файла считываем пустую строку
        break
    else:
        lst2.append(stro)
lst2.reverse()
count = 1
for i in lst2:
    if count  < len(lst2):
        f2.write(i+'\n') # во все строки кроме последней добавляем перенос строки
        count +=1
    else:
        f2.write(i) # в последнюю строку перенос строки не добавляем

print(lst2)
f1.close()
f2.close()
'''

'''
import sys
sys.path.insert(1, './pages')
'''

'''
import os
import os.path
print(os.listdir('c:/FAR'))
print(os.listdir())# содержание текущей директории
current_dir = os.getcwd()
print(current_dir)
print(os.pardir)
#os.chdir(os.pardir)
print(current_dir)
print(os.path.exists('main.py'))
print(os.path.isfile('main.py'))
print(os.path.isdir('main.py'))
print(os.path.abspath('main.py'))
#for current_dir, dirs, files in os.walk("."):
    #print(current_dir, dirs, files)

#import shutil
#shutil.copy('test.txt', 'test25.txt')
#shutil.copytree('test', 'test/test')# копируем каталог целиком

'''

'''
n, k = map(int, input().split())
print(n + k)
'''

'''
x = input().split()
print(x)

map_obj = map(int, x)
print(next(map_obj))
print(next(map_obj))
'''


'''
x = input().split()
k = [int(i) for i in x]
print(k)
'''

'''
x = input().split()
k, n = (int(i) for i in x)
print(k+n)
'''


'''
x = input().split()
xs = (int(i) for i in x)

print(xs)
def eaven(a):
    return a % 2 ==0

p = filter(eaven, xs)
print(p)
for j in p:
    print(j)
'''



'''
x = input().split()
xs = (int(i) for i in x)

eaven = lambda x: x % 2 == 0
eavens = list(filter(eaven, xs))
print(eavens)
'''

'''
x = input().split()
xs = (int(i) for i in x)
eavens = list(filter(lambda x: x % 2 == 0, xs))
print(eavens)
'''

'''
x = [('Guido',  'Van',  'Rossum'), ('Huskil', 'Carry'), ('John', 'Backus')]
def length(name):
    return len(' '.join(name))

name_length = [length(name) for name in x]
print(name_length)
s = sorted(x, key=length)
p = sorted(x, key=lambda name: len(' '.join(name)))
print(s)
print (p)
'''


'''
student = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ]

# Сортируем по убыванию возраста student[2]
x = sorted(student, key=lambda i: i[2], reverse=True)
print(x)
'''

'''
student = [
    ('john', 15, 4.1),
    ('jane', 12, 4.9),
    ('dave', 10, 3.9),
    ('kate', 11, 4.1),
    ]

from operator import itemgetter
x = sorted(student, key=itemgetter(2,1))
print(x)
'''

'''
from functools import partial
x = int('1101', base=2)
print(x)
int2= partial(int, base=2)
x = int2('1101')
print(x)

sort_by_last = partial(list.sort, key=itemgetter(-1))
y = ['abc', 'cba', 'abb']
sort_by_last(y)
print(y)
'''
'''
import operator
inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]

print(list(map(operator.itemgetter(1), inventory)))
# [3, 2, 5, 1]
print(sorted(inventory, key=operator.itemgetter(1)))
# [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]
'''


#word = word[:word.index(' ')]# Теперь Word это все символы до первого пробела





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

#print("abc" in "abcba")
#print("abce" in "abcba")
#p = 'cabcd'
#print(p.find('d'))
#print("cabcd".find("abc", 1))  # индекс первого вхождения или -1
#print("cabcd"[1:].find("abc"))
#print(str.find.__doc__)

'''
s = 'asadfa'
print(s[1:3])
'''

#print("cabcd".index("abc"))  # индекс первого вхождения или ValueError


#s = "The woman in black fled across the desert, and the gunslinger followed"
#print(s.startswith(("The woman", "The dog", "The man in black")))
# print(s.startswith.__doc__)

#s = "image.png"
#print(s.endswith(".png"))

#s = "abacaba"
#print(s.find("aba", 0))
#print(s.count("aba"))
# print(s.count.__doc__)

#print(s.rfind("aba"))

#s = "The man in black fled across the desert, and the gunslinger followed"
#print(s.lower())
#print(s.upper())
#print(s.count("the"))
#print(s.lower().count("the"))

#s = "1,2,3,4"
#print(s)
#print(s.replace(",", ", ", 2)) # заменим только два вхождения
#print(s.replace.__doc__)

#s = "1\t\t 2  3       4       "
#print(list(map(int,(s.split()))))
s = '1  2 3 4'
#print(s.split(" ", 2))# только два разделения
#print(s.split())

# print(s.split.__doc__)

#s = "_*__1, 2, 3, 4__*_"
#print(repr(s.rstrip("*_")))
#print(repr(s.lstrip("*_")))
#print(repr(s.strip("*_")))
#ss = '12558     '
#ssa = ss.rstrip()
#print(ssa)

#numbers = map(str, [1, 2, 3, 4, 5])
#print(repr(" ".join(numbers)))


#capital = 'London is the capital of Great Britain'
#template = '{} is the capital of {}'
#print(template.format("London", "Great Britain"))
#print(template.format("Vaduz", "Liechtenstein"))
#print(template.format.__doc__)


#template = '{capital} is the capital of {country}'
#print(template.format(capital="London", country="Great Britain"))
#print(template.format(country="Liechtenstein", capital="Vaduz"))

'''
import requests
template = "Response from {0.url} with code {0.status_code}"
#
res = requests.get("https://docs.python.org/3.5/")
print(template.format(res))
#
res = requests.get("https://docs.python.org/3.5/random")
print(template.format(res))

from random import random
x = random()
print(x)
print("{:.3}".format(x))
'''

'''
#s, a, b = input().split()
s = 'ababa'
a = 'a'
b = 'b'
count = 0
while a in s:
    s = s.replace(a, b)
    count += 1
    if count == 1000:
        print('Impossible')
        break

print(count)
'''

'''
s = "abababaaba"
t = "aba"
count = 0
l = len(s)

for i in range(0, l):
    if s.startswith(t):
        count += 1
    s = s[1:]
print(count)
'''

'''
x = 'hello\nworld'
print(x)
x = r'hello\nworld'
print(x)
import re
pattern = r'abc'
string = 'abc'
match_objeckt = re.match(pattern, string)
print(match_objeckt)

'''
'''
import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))
'''


'''
import os, os.path
#(__file__) - текущий исполняемый файл
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
#print(current_dir)

file_path = os.path.join(current_dir, 'file.txt')
#print(file_path)
print(os.path.abspath(__file__))

print(os.path.dirname(__file__))

'''

'''
f =3
g =5
c = f if g > 5 else None
print(c)
'''

'''
class Gross:
    a = [2,3,4,5,6,6,7]
    print(a[1:5])
    print(a[4:])
    print(len(a))

b = Gross()
print(b.__class__)
print(b.__class__.__module__.split('.')[0:])
'''

'''
params = {'param1': 1, 'param2': 2, 'param3': 3}
param_string = '\n'.join(["{0}: {1}".format(k, v) for k, v in params.items()])
print(param_string)
import json
print(json.dumps(params))
'''

'''
class MyClass:
    def __init__(self, url):
        self.url = url

    def get_url(self, path):
        return '{0}/{1}'.format(self.url, path.strip('/'))

obj = MyClass('http://www.example.com')
print(obj.get_url('/test/path/'))
'''

'''
message = "Hello"
message += f"""
This is a multiline string.
It's part of the message.
"""
print(message)
'''

'''
resp_status_code = 100
status_code = 200
ok = resp_status_code == status_code
'''

'''
import csv
with open('example.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open('example.csv') as f:
    reader = csv.reader(f, delimitre="\t")
    for row in reader:
        print(row)
students =  [
    ["Greg", "Dean", 70,80,90,"Good job, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely Done"]
]
with open('example.csv', "a") as f:
    writter = csv.writer(f)
    #writter.writerows(students)
    for student in students:
        writter.writerow(student)
'''

'''
import uuid
session_id = str(uuid.uuid4())
print(session_id)
'''

'''
lst = [1,2,25,3,4,5,5]
print(sorted(lst))
print(lst)
lst.sort()
print(lst)
'''

'''
a = [1, 2, 3]
b = ["one", "two", "three"]

for val1, val2 in zip(a, b):
    print(val1, val2)

for val1, val2 in enumerate(a):
    print(val1, val2)
'''


'''
from itertools import chain
# Suppose we have the following dictionary:
res = {
    'key1': ['value1', 'value2'],
    'key2': ['value3', 'value4', 'value5'],
    'key3': ['value6']
}




length = len(list(chain(*list(res.values()))))
print(res.values())
print(list(res.values()))
print(*list(res.values()))
print(chain(*list(res.values())))
print(list(chain(*list(res.values()))))
'''

'''
from itertools import chain
it1 = range(1, 6)
it2 = range(10, 16)
rez = chain(it1, it2)
list(rez)
'''

from datetime import datetime

today_year = datetime.today().year
print(today_year)

