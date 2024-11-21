

from itertools import chain
it1 = range(1, 6)
it2 = range(10, 16)
rez = chain(it1, it2)
for i in rez:
    print(i)


from itertools import chain
# Suppose we have the following dictionary:
res1 = {
    'key1': ['value1', 'value2'],
    'key2': ['value3', 'value4', 'value5'],
    'key3': ['value6']
}

res = {
    "2": [
        {
            "id": 5,
            "size": " - 4 + 3 ",
            "weight": 5,
            "cost": 4
        },
        {
            "id": 6,
            "size": " - 5 + 4 ",
            "weight": 3,
            "cost": 13
        }
    ],
    "3": [
        {
            "id": 7,
            "size": " - 6 + 5 ",
            "weight": 14,
            "cost": 5
        },
        {
            "id": 8,
            "size": " - 7 + 6 ",
            "weight": 4,
            "cost": 4
        },
        {
            "id": 9,
            "size": " - 9 + 7 ",
            "weight": 9,
            "cost": 14
        }
    ],
    "4": [
        {
            "id": 10,
            "size": " - 11 + 9 ",
            "weight": 12,
            "cost": 11
        }
    ],
    "5": [
        {
            "id": 11,
            "size": " - 12 + 11 ",
            "weight": 8,
            "cost": 8
        },
        {
            "id": 12,
            "size": "2GR",
            "weight": 4,
            "cost": 5
        }
    ],
    "6": [
        {
            "id": 13,
            "size": "3GR",
            "weight": 7,
            "cost": 2
        }
    ],
    "7": [
        {
            "id": 14,
            "size": "4GR",
            "weight": 11,
            "cost": 11
        },
        {
            "id": 15,
            "size": "5GR",
            "weight": 1,
            "cost": 10
        },
        {
            "id": 16,
            "size": "6GR",
            "weight": 12,
            "cost": 2
        }
    ],
    "8": [
        {
            "id": 2047,
            "size": " + 1, 8CT",
            "weight": 10,
            "cost": 11
        }
    ]
}

print(res.items())
print(list(res.items()))
length = len(list(chain(*list(res.values()))))
print(length)
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



ll = ((99, 89, 97),)
a = list(*chain(ll))
print(a)

ll = ((99, 89, 97),)
a = list(chain(*ll))
print(a)

ll = ((99, 89, 97), (25, 17))
a = list(chain(*ll))
print(a)

ll = ((99, 89, 97))
a = list(chain(ll))
print(a)