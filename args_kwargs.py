
first, second, *other = [1,2,3,4,5,6,7]
print(first)
print(second)
print(other)

def sum_of_three(a, b, c):
    return a + b + c
three = [1, 2, 3]
print(sum_of_three(*three))

def print_ab(a, b=50):
    print(a)
    print(b)
args = {'a': 10, 'b': 20}
lst = [11, 12]
print_ab(**args)
print_ab(*args)
print_ab(*lst)




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

