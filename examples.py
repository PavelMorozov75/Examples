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

'''
from datetime import datetime

today_year = datetime.today().year
print(today_year)
'''

'''
working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
employees_2 = {}.fromkeys(working_days, 0)
print(employees_2)
'''


'''
import pytest

from datetime import datetime, timedelta

testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected
'''

'''
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
new_dict = {k: v for k, v in my_dict.items() if k != 'banana'}

my_dict[None] = 5
print(my_dict)
'''

'''
from oop_examples import CC
import sys, os
class A:
    pass
print (sys.modules)
print(sys.modules[A.__module__])
print(sys.modules[A.__module__].__file__)

print('CC.__module__  ', CC.__module__)
print('sys.modules[CC.__module__]   ', sys.modules[CC.__module__])
print('sys.modules[CC.__module__].__file__   ', sys.modules[CC.__module__].__file__)


print('__name__ ', __name__)
print('__file__', __file__)
print('sys.argv  ', sys.argv)
print('os.getcwd()  ', os.getcwd())
'''

'''
dd = {}
dd[None] = 3
print(dd)
'''


'''
import os
print(dict(os.environ))
for key, value in os.environ.items():
    print(key, '', value)
'''

'''
print(100//13)
print(100%13)
'''

'''
from random import randint, choice
seq_sum = 200
quantity = 7

medium = seq_sum // quantity
print('medium ', medium)
mod = seq_sum % quantity
print('mod ', mod)

result = [medium + 1 * (j < mod) for j in range(quantity)]
print(sum(result))
print(result)

print(len(result) // 2)

for i in range(len(result) // 2):
    value = randint(1, min(result[i], result[-(i + 1)] - 1)) * (-1) * choice((-1, 1))
    print('value ', value)
    result[i] += value
    print(result[i])
    result[-(i + 1)] -= value
    print(result[-(i + 1)])

print(tuple(result))
print(sum(result))
'''

'''
from random import randint
weights = [randint(10 ** i, 10 ** (i + 1)) for i in range(10)]
costs = [randint(10 ** i, 10 ** (i + 1)) for i in range(10)]
print(weights)
print(costs)
'''


'''
from decimal import Decimal
number = 3.25887
acc =0

exp = f"1{'.' * bool(acc)}{'0' * acc}"
print(bool(acc))
print('.' * bool(acc))
print('0' * acc)
print('exp = ', exp)

res = float(Decimal(str(number)).quantize(Decimal(exp)))
res1 = Decimal(str(number)).quantize(Decimal(exp))
print(res)
print(res1)
'''

'''
import pytest_testrail
import pytest
from pytest_testrail.plugin import pytestrail
for i in range(0, 6, 2):
        with subtests.test(i=i):
            assert i % 2 == 0
'''

'''
x = {'one': 0, 'two': 20, 'three': 3, 'four': 4}
xx = x.setdefault('six', 6)
print(xx)

'''

'''
import datetime
from datetime import timedelta


date = datetime.datetime(2023, 10, 30, )
month_to_add = 47

years = int(month_to_add / 12)
print(years)
month = abs(month_to_add) % 12
print(month)
if month_to_add < 0:
    month *= - 1

new_month = (date.month + month) % 12 or 12
print('date.month', date.month)
nw = (date.month + month) % 12
print('nw', nw)
print('new_month', new_month)

years += (date.month + month) // 13
print('years ', years)

aa = date.replace(year=date.year + years, month=new_month)
print(aa)
'''

'''
import collections
c = {'weight': 1100.0, 'cost': 2000.0}
b = {'weight': 7974.88, 'cost': 2338806.97}
c1 = collections.Counter(c)
b1 = collections.Counter(b)
# print(c1+b1)
'''


lst = [{'id': 1, 'val':1}, {'id': 2, 'val':3}, {'id': 1, 'val':4}]
def f(lst):
    dct = {}
    for x in lst:
        if x['id'] in dct:
            dct[x['id']] += x['val']
        else:
            dct[x['id']] = x['val']
    print(dct)
    return [{'id': x, 'val': y} for x, y in dct.items()]

print(f(lst))



lst2 = [{'id': 1, 'val':1, 's': 5}, {'id': 2, 'val':3, 's': 8}, {'id': 1, 'val':4, 's': 15}]
def f2(lst):
    dct = {}
    for x in lst:
        if x['id'] in dct:
            dct['id'] = x['id']
            dct['val'] += x['val']
            dct['s'] += x['s']

        else:
            dct['id'] = x['id']
            dct['val'] = x['val']
            dct['s'] = x['s']
    return dct
print(f2(lst2))





from functools import reduce
data = [{'id': 'a', 'val': 1, 'a': 7}, {'id': 'b', 'val':3, 'a': 9 }, {'id': 'a', 'val':4, 'a': 14}, {'id': 'b', 'val': 8, 'a': 50 } ]
def f(d, x):
    k = x['id']
    if k in d:
        d[k]['val'] += x['val']
        d[k]['a'] += x['a']
    else:
        d[k] = x
    return d
#print (reduce(f, data, {}))
print (list(reduce(f, data, {}).values()))

'''
data = [{'id': 1, 'val':1, 'a': 'd'}, {'id': 2, 'val':3, 'a': 'b' }, {'id': 1, 'val':4, 'a': 'c'} ]
def f(d, x):
    k = x['id']
    if k in d:
         d[k]['val'] = max(x['val'] for d in data)
    else:
        d[k] = x
    return d
print reduce(f, data, {}).values()
'''