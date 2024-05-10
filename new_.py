class MyClass:
    def __new__(cls, *args, **kwargs):
        print('Запустился __new__')
        return super().__new__(cls)

    def __init__(self):
        print('Запустился __init__')

my_instance = MyClass()


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()

print(a is b)  # True

class ImmutableString(str):
    def __new__(cls, value):
        return super().__new__(cls, value.upper())

s = ImmutableString("lalala")
print(s)  # "HELLO"


class StopNumber:

    def __new__(cls, number, name):
        # cls.number = number
        # cls.name = name
        if number > 1000:
            return super().__new__(cls)
        else:
            pass

    def __init__(self, number, name):
        self.number = number
        self.name = name

# Код ниже пожалуйста не меняйте
Masha = StopNumber(500, 'Masha')
Vika = StopNumber(1500, 'Vika')
Lena = StopNumber(1200, 'Lena')

print(isinstance(Masha, StopNumber))
print(isinstance(Vika, StopNumber))
print(isinstance(Lena, StopNumber))



class StopNumber(int):

    def __new__(cls, number):

        if number > 1000:
            return super().__new__(cls, number)
        else:
            pass

    def __init__(self, number):
        self.number = number


# Код ниже пожалуйста не меняйте
Masha = StopNumber(1500)
print(isinstance(Masha, StopNumber))
print(Masha.number)

class Alfa:
    def __new__(cls, x):
        cls.x = x + 200
        return super().__new__(cls)

    def __init__(self, x):
        self.x = x

beta = Alfa(200)
print(beta.x, Alfa.x)



'''
class StopNumber:
    def __new__(cls, number, name):
        if number > 1000:
            return super().__new__(cls, number + 100, name)

    # def __init__(self, number, name):
    #     self.number = number
    #     self.name = name


# Код ниже пожалуйста не меняйте
Masha = StopNumber(500, 'Masha')
Vika = StopNumber(1500, 'Vika')
Lena = StopNumber(1200, 'Lena')

print(isinstance(Masha, StopNumber))
print(isinstance(Vika, StopNumber))
print(isinstance(Lena, StopNumber))
'''