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
class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self, x):
        if x > 0:
            # super(PositiveList, self).append(x)
            super().append(x)
        else:
            raise NonPositiveError




a = PositiveList()
a.append(3)
print(a)
a.append(-8)
'''

class BeautyTransform:

    def __init__(self, height, weight=0):
        self.height = height
        self.weight = weight

    def transformer(self):
        try:
            new_body = self.height / self.weight
            print('Успешная трансформация')
            return new_body
        except ZeroDivisionError:
            print('Лицо как в картине Крик, Эдварда Мунка')


vasya = BeautyTransform(172, 70)
nastya = BeautyTransform(100, 50)
lena = BeautyTransform(50)

vasya.transformer()
nastya.transformer()
lena.transformer()

class BeautyTransform:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.result = "Божественная красота"

    def transformer(self):
        try:
            self.new_body =  self.height / self.weight
        except Exception:
            self.result = "Индюк на три дня"
        else:
            print(f"Проверка прошла!", end=' ') #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        finally:
            print(f"Результат: {self.result}")



# Код ниже пожалуйста не меняйте, ради Васи
nastya = BeautyTransform(100, 50)
lena = BeautyTransform(50, 90)
vasya = BeautyTransform(172, "Индюк")

nastya.transformer()
lena.transformer()
vasya.transformer()