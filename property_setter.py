

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