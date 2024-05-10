
from examples import C
class A:
    pass
class B:
    pass


a = A()
print(a.__class__)
print(C.__module__)
print(a.__module__)
print(__name__)
print(a.__class__.__module__)
print('C.__class__.__module__   ', C.__class__.__module__)
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