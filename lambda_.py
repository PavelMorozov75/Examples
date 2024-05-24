add_l = lambda x, y: x + y
print(add_l( 3,7))


print((lambda x, y: x +y)(15, 25))

from math import pi
compute_square = {'circle': lambda r: pi*r**2, 'rectangle': lambda a, b: a * b}
print(compute_square)
print(compute_square['circle'](5))
print(compute_square['rectangle'](5,10))


xs = [3, 14, 15, 92, 65]
max_index = max((0, 1, 2, 3, 4), key=lambda i: xs[i])
print(max_index)



'''
def print_smth1(a):
    print(a)

def print_smth2(a, b):
    print(a, b)

actions = {1: print_smth1("text"),
           2: print_smth2("text1", "text2")}

s = 1
action = actions.get(s)
action()
'''


from functools import partial

def print_smth1(a):
    print(a)

def print_smth2(a, b):
    print(a, b)

actions = {1: partial(print_smth1, 'text'),
           2: partial(print_smth2, 'text', 'text2')}

s = 1
action = actions.get(s)
action()


def print_smth1(a):
    print(a)

def print_smth2(a, b):
    print(a, b)

actions = {1: lambda: print_smth1("text"),
           2: lambda: print_smth2("text1", "text2")}

s = 2
action = actions.get(s)
action()
