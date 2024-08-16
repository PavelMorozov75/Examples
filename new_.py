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
        return super().__new__(cls, value.upper()+'hh')

s = ImmutableString("lalala")
print(s)  # "LALALAhh"


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
        cls.number = number
        if cls.number > 1000:
            return super().__new__(cls, cls.number + 25)
        else:
            pass

    # def __init__(self, number):
    #     self.number = number


# Код ниже пожалуйста не меняйте
Masha = StopNumber(10100)
print(isinstance(Masha, StopNumber))
print("Masha.number", Masha.number)

'''
class Alfa:
    def __new__(cls, x):
        cls.x = x + 200
        return super().__new__(cls)

    def __init__(self, x):
        self.x = x

beta = Alfa(200)
print(beta.x, Alfa.x)
'''



class StopNumber(int):
    
    def __new__(cls, number):
        if number > 1000:
            return super().__new__(cls, number + 100)

    # def __init__(self, number):
    #     self.number = number



# Код ниже пожалуйста не меняйте
Masha = StopNumber(1500)
print(Masha)

# Vika = StopNumber(1500, 'Vika')
# Lena = StopNumber(1200, 'Lena')

# print(isinstance(Masha, StopNumber))
# print(isinstance(Vika, StopNumber))
# print(isinstance(Lena, StopNumber))

class Word(str):
    '''Класс для слов, определяющий сравнение по длине слов.'''

    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print ("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] # Теперь Word это все символы до первого пробела
        return str.__new__(cls, word)

ww = Word('yyyy iii')
print(ww)