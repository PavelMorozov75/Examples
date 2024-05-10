
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
