

from itertools import chain
it1 = range(1, 6)
it2 = range(10, 16)
rez = chain(it1, it2)
for i in rez:
    print(i)


from itertools import chain
# Suppose we have the following dictionary:
res = {
    'key1': ['value1', 'value2'],
    'key2': ['value3', 'value4', 'value5'],
    'key3': ['value6']
}




length = len(list(chain(*list(res.values()))))
print(res.values())
print(list(res.values()))
print(*list(res.values()))
print(chain(*list(res.values())))
print(list(chain(*list(res.values()))))


a = [1, 2, 3]
b = ["one", "two", "three", "four", "five"]

for val1, val2 in zip(a, b):
    print(val1, val2)

s = 'abc'
t = (10, 20, 30, 40)
print(list(zip(s,t)))




for val1, val2 in enumerate(a):
    print(val1, val2)