


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
'''

'''
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
'''



'''
from functools import reduce #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
data = [{'id': 'a', 'val': 1, 'a': 7}, {'id': 'b', 'val':3, 'a': 9 }, {'id': 'a', 'val':4, 'a': 14}, {'id': 'b', 'val': 8, 'a': 50 }, {'d': 'b', 'val': 8, 'a': 50}  ]
def f(d, x):
    k = x.get('id')
    print('d', d)
    print('x', x)
    if k in d:
        d[k]['val'] += x['val']
        d[k]['a'] += x['a']
    else:
        d[k] = x
    return d
print (reduce(f, data, {}))
#print (list(reduce(f, data, {}).values()))
'''


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


'''
lst = [['45'], ['43'], ['35'], ['33'], ['29'], ['27'], ['45', ' 43', ' 35', ' 33', ' 29', ' 27']]
lst2 = [['198', ' 193', ' 189', ' 184', ' 180', ' 177', ' 172']]


def make_norm_list(lst):
    new_lst = []
    for item in lst:
        if len(item) > 1:
            for item_item in item:
                if item_item.strip()[0] not in new_lst:
                    new_lst.append(item_item.strip()[0])
        else:
            new_lst.append(item[0])
    return new_lst

lst3 = ['111', '111', '111, 16, 15']

def make_norm_list2(lst):
    new_lst = []
    for item in lst:
        if ',' in item:
            item_lst = item.split(',')
            for item_item in item_lst:
                if item_item.strip() not in new_lst:
                    new_lst.append(item_item.strip())
        else:
            if item not in new_lst:
                new_lst.append(item)
    return new_lst
print(make_norm_list2(lst3))
'''





'''
from distutils import util

def type_bool(x: str) -> bool:
    return bool(util.strtobool(x))

# Example usage
print(type_bool("true"))  # Output: True
print(type_bool("f"))  # Output: True
'''


'''
parent = page = None
print(parent, page)
'''

'''
from dataclasses import dataclass, asdict

@dataclass
class Option:
    name: str
    default_value: str
    type: type
    help: str

# Create an Option object
option = Option("BASE_URL", "", type=str, help="example help")

# Convert the Option object to a dictionary and filter out None values
option_dict = {k: v for k, v in asdict(option).items() if v is not None}

print(option_dict)
'''
'''
import os
print(os.environ)
# for key, value in os.environ.items():
#     print(key, value)
'''



'''
def line(n, newline):
    aa = ('\n' if newline else ' ').join('Вася' * n)
    return aa

print(line(5, False))
'''


a = 1
b = None
print(f"Вариант 1 : a = {a}, b = {b} ")
print(a and b is None)
print(not (a and b is None), '\n')

a = None
b = 1
print(f"Вариант 2 : a = {a}, b = {b} ")
print(a and b is None)
print(not (a and b is None), '\n')

a = None
b = None
print(f"Вариант 3 : a = {a}, b = {b} ")
print(a and b is None)
print(not (a and b is None))

print('\n')
print(None and True)#None
print(None and False)#None
print(None or True)#True
print(not None)#True

'''
class C:
    pass



__all__ = [C]
'''

'''
from cssselect import GenericTranslator, SelectorError
try:
    expression = GenericTranslator().css_to_xpath('div.content')
except SelectorError:
    print('Invalid selector.')

print(expression)
'''

#print('туториал', 'по', 'функции', 'print()', sep='\n\n') #sep - символ между словами
'''
import string, random
def generate_name(length):
    all_symbols = string.ascii_letters
    name = ''.join(random.choice(all_symbols) for _ in range(length))
    return name

print(generate_name(7))
'''

import uuid
from random import randint
session_id = str(uuid.uuid4())
print(session_id)

'''
count_rooms = 1
roomlist = [{"id": str(uuid.uuid4()), "name": randint(100, 999), "isActive": True} for _ in range(count_rooms)]
print(roomlist)
'''

'''
print(11%12)
print(13//13)
'''
'''
from sys import getdefaultencoding
print(getdefaultencoding()) # utf-8
my_bytes = 'котобус cat'.encode()
print(my_bytes)#b'\xd0\xba\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb1\xd1\x83\xd1\x81 cat'
print(my_bytes.decode())
# 'котобус cat
# print(my_bytes.decode('ascii', errors='surrogateescape'))
'''
a = [('458',)]
b = a[0]

boxes = [2, 2] #список изложниц с количеством камней
stones_count = sum(boxes)
print(stones_count)
