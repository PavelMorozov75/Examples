#https://stepik.org/lesson/63305/step/1
#https://stepik.org/lesson/63306/step/1

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
print(identity.__name__)

'''
def memorized(func):
    memory = {}
    def wrapper(*args, ** kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in memory:
            memory[key] = func(*args, **kwargs)
        return memory[key]
    return wrapper

def collatz_sequenze(n):
    while n!= 1:
        print(n)
        n = (3*n + 1) if n % 2 else (n // 2)

t = memorized(collatz_sequenze)
print(t(22222222222222222222222))
print(t(22222222222222222222222))
'''
'''
def memorized_1(func):
    memory = {}
    def wrapper(*args, ** kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in memory:
            memory[key] = func(*args, **kwargs)
        return memory[key]
    return wrapper
@timed
@memorized_1
def collatz_sequenze_1(n):
    while n!= 1:
        print(n)
        n = (3*n + 1) if n % 2 else (n // 2)


print(collatz_sequenze_1(22222222222222222222223))
print(collatz_sequenze_1(22222222222222222222223))
'''

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

'''
call_count = 0
def call_counter_hook(func):
    def wrapper(*args, **kwargs):
        global call_count
        call_count += 1
        return func(*args, **kwargs)

    return wrapper

@call_counter_hook
def my_function():
    print("Выполняется основная функция")


for _ in range(5):
    my_function()

print(f"Функция вызвана {call_count} раз")  # Вывод: Функция вызвана 5 раз
'''


def make_wrapper_decorator(func):
    def wrapper_decorator(wrap):
        wrap.__name__ = func.__name__
        wrap.__doc__ = func.__doc__
        return wrap  # 3)возврат wrapper обратно во wrapper с переписанными аттрибутами

    return wrapper_decorator


def decorator(func):

    #@make_wrapper_decorator(func)  # 2)wrapper = make_wrapper_decorator(func)(wrapper) т.е. =wrapper_decorator(wrapper)

    wrapper_decorator = make_wrapper_decorator(func)   #

    @wrapper_decorator
    def wrapper(*args, **kwargs):
        print(wrapper.__name__)  # div
        args = reversed(args)
        return func(*args, **kwargs)

    return wrapper


@decorator  # 1)здесь начало: div = flip(div)
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)  # 2.0
    return res


div(2, 4, show=True)
print(div.__name__)  # div




import functools
def decorator1(func):

    @functools.wraps(func)  # 2)wrapper = make_wrapper_decorator(func)(wrapper) т.е. =wrapper_decorator(wrapper)
    def wrapper(*args, **kwargs):
        print(wrapper.__name__)  # div
        args = reversed(args)
        return func(*args, **kwargs)

    return wrapper


@decorator1  # 1)здесь начало: div = flip(div)
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)  # 2.0
    return res


div(2, 10, show=True)
print(div.__name__)  # div


class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        result *= 2
        print(result)

@Decorator
def my_function(x, y):
    return x + y

my_function(10, 5)  # 30

# Метод __call__ имеет один параметр (number) и делает подсчёт, через сколько лет экземпляру будет number лет.
# В нашем случае, мы будем вставлять число 20. Метод возвращает результат (return).
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self(20))

    def __call__(self, number):
        return 20 - self.age

masha = Person('Masha', 9)
vasya = Person('Vasya', 19)