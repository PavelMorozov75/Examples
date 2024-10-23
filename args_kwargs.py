
first, second, *other = [1,2,3,4,5,6,7]
print(first)
print(second)
print(other)

def sum_of_three(a, b, c):
    return a + b + c
three = [1, 2, 3]
print('sum_of_three ', sum_of_three(*three))

def print_ab(a, b=50):
    print(a)
    print(b)
args = {'a': 10, 'b': 20}
lst = [11, 12]
print_ab(**args)
print_ab(*args)
print_ab(*lst)

def print_abc (*aargs): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    print('additional arguments ')
    for arg in aargs:
        print(arg)
print_abc(1)
ll = [33,34,35]
print(ll)
print(*ll)

def print_abcd(**kwargs): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print('additional arguments ')
    for key in kwargs:
        print(key, kwargs[key])

print_abcd(c=85, d=87, e=88)
dd = {"c": 3, "d": 25}
print_abcd(**dd)




def print_abc (a, b , *aargs):
    print('positional argument 1 = ', a)
    print('positional argument 2 = ', b)
    print('additional arguments ')
    for arg in aargs:
        print(arg)
print_abc(1,2, 25, 26, 27)



def print_abcd (a, b , **kwargs):
    print('positional argument 1 = ', a)
    print('positional argument 2 = ', b)
    print('additional arguments ')
    for key in kwargs:
        print(key, kwargs[key])
print_abcd(10, 20, c=85, d=87, e=88)
print_abcd(10, c=85, d=87, e=88, b=1)



def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

#print(s(b=31))
#s(b=31, 0)
print(s(11, 10, 10))



def aa(*args, **kwargs):
    print(args)
    print(kwargs)

a = {'c': 1, 'b': 7, 'z': 38 ,'a': 25}
b = {k : v for k, v in a.items()}
c = [1,3,4,5]

aa(*c, **a)
print('b ', b)


def wrapper(*args, **kwargs):
    key = (args, (sorted(kwargs.items())))
    print(key)

a = {'c': 1, 'b': 7, 'z': 38 ,'a': 25}
c = [1,5,4,7]
wrapper(*c, **a)
wrapper(1, 10, 25, c=56, a=2)

day_offs = ['суббота', 'воскресенье']
workdays =['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
weekends = ['пятница','суббота','воскресенье']

res = [*day_offs, *[x for x in weekends if x not in workdays]]
print(res)

list1 =['Петя', 'Вася', 'Сережа']
emploee = 'Павел'

def print_emploee(*emploees):
    print(emploees)
    for emploee in emploees:
        print(emploee)

print_emploee(*list1, emploee)
print_emploee((*list1, emploee))
print_emploee(list1)
print_emploee(emploee)
