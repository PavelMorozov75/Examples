
from examples import C
class A:
    def __init__(self, x):
        self.x = 3
    def aaa(self):
        pass

class B(A, C):

    c = str
    def bbb(self):
        self.z = str




a = A(3)
b = B(5)
print(a.__class__)
print(C.__module__)
print(a.__module__)
print(__name__)
print(a.__class__.__module__)
print('C.__class__.__module__   :', C.__class__.__module__)
print("B.__mro__ :", B.__mro__)
print('dir(B)   :', dir(B))

a = B.__mro__
for element in a:
    for key, value in element.__dict__.items():
        print(key, value)
#  не работает  print(a.__class__.__module__.__file__)
#  не работает  print(a.__class__.__file__)




from oop_examples import CC
import sys, os
class A:
    pass
print (sys.modules)
print('sys.modules[A.__module__] : ', sys.modules[A.__module__])
print('sys.modules[A.__module__].__name__ : ', sys.modules[A.__module__].__name__)
print('sys.modules[A.__module__].__file__ : ', sys.modules[A.__module__].__file__)

print('CC.__module__  ', CC.__module__)
print('sys.modules[CC.__module__]   ', sys.modules[CC.__module__])
print('sys.modules[CC.__module__].__file__   ', sys.modules[CC.__module__].__file__)


print('__name__ ', __name__)
print('__file__', __file__)
print('sys.argv  ', sys.argv)
print('os.getcwd()  ', os.getcwd())