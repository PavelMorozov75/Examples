

def identity(x):
    return x

f = identity
for attribute in (f.__name__, f.__module__, f.__doc__, f.__class__):
    print(attribute)

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

# производная
def D(f):
    def derivative(x):
        return (f(x + 0.000001) - f(x))/0.000001
    return derivative

def f(x):
    return x**2

d = D(f)
print(d(5))
print(D(f(5)))

#замыкание
def make_greeter(phrase):
    prefix = phrase + ' , '
    def greeter(name):
        return prefix + name
    return greeter
casual_greeter = make_greeter('Hallo')
informal_greeter = make_greeter(('Sup'))
mysterios_greeter = make_greeter(('So we meet again'))

print('\n'.join((casual_greeter('World'), informal_greeter('Dvach'), mysterios_greeter('my heartach'))))

#замыкание
def composition(f, g):
    def h(x):
        return f(g(x))
    return h
h = composition(lambda x: x**2, lambda x: x + 1)
print(h(5))



from time import time
def timed(func):
    def timed_func(*args, **kwargs):
        tmp = time()
        result = func(*args, **kwargs)
        print(result)
        print(func.__name__, 'executed, time: ', time() - tmp)
        return result
    return timed_func

def f1(x, y):
    return x + y

t1_func = timed(f1)
t1_func(6, 3)

def introduce(func):
    def wrapper(*args, **kwargs):
        print('Function name ', func.__name__)
        return func(*args,**kwargs)
    return wrapper
@introduce
def identity(x):
    return x
print(identity(5))

'''
from time import time
def timed(func):
    def timed_func(x, y):
        tmp = time()
        result = func(x, y)
        print(result)
        print(func.__name__, 'executed, time: ', time() - tmp)
        return result
    return timed_func

def f1(x, y):
    return x + y
t1_func = timed(f1)
t1_func(2,3)
'''
