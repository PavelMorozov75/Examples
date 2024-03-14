
lst = [1, 2, 3, 34]
book = {'author': 'Pushkin', 'title': 'Golden Fish', 'year': 1785}
str = 'Hallo for all'

for i in lst:
    print(i)
for i in book:
    print(i)

iterator = iter(lst)
a = next(iterator)
b = 1 + next(iterator)
print(a)
print(b)

it = iter(book)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break




'''
from random import random
class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0
    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration
    def __iter__(self):
        return self

x = RandomIterator(3)
#print(next(x))
#print(next(x))
#print(next(x))
for i in x:
    print(i)
'''



class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i -2], self.lst[self.i -1]
        else:
            raise StopIteration

class Mylist(list):
    def __iter__(self):
        return(DoubleElementListIterator(self))


for pair in Mylist([1,2,2,4]):
    print((pair))



from random import random
def random_generator(k):
    for i in range(k):
        for j in ['a', 'b']:
            yield {j: random()}

gen = random_generator(2)
#print(next(gen))
#print(next(gen))
#print(next(gen))
print(gen)
for i in gen:
    print(i)



def brand_new_iterator():
    i = 0
    while True:
        yield i
        i += 2
        yield i
        i += 1

list1 = []
itrtr = brand_new_iterator()
for i in range(10):
    list1.append(next(itrtr))
print(list1)
