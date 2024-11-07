

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname


    # сеттер для свойства full_name
    @full_name.setter
    def full_name(self, new):
        self.name, self.surname = new.split(' ')

tom = Person('Thomas', 'Smith')

print(tom.surname)
print(tom.full_name) # 'Thomas Smith' без скобок !!!!!!!


tom.full_name = 'Alice Cooper'
print(tom.name)  # 'Alice'
print(tom.surname)  # 'Cooper'


class IPAddress:

    def __init__(self, address, mask):
        self._address = address
        self._mask = int(mask)

    @property
    def mask(self):
        return self._mask

ip1 = IPAddress('10.1.1.1', 24)
print(ip1.mask + 1) #!!!!!!!!!!!!!!!!!!!!!! не ip1.mask() !!!!!!!!!!!!!!!!


class Car:

    # создаем конструктор класса Car
    def __init__(self, model):
        # Инициализация свойств.
        self.model = model

    # создаем свойство модели.
    @property
    def model(self):
        return self.__model

    # Сеттер для создания свойств.
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return "Год выпуска модели " + str(self.model)


carA = Car(2019)
print(carA.model)
print(carA.getCarModel())