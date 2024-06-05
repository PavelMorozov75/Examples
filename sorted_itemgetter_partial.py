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
