
variable = [i*i for i in range(10) if i > 5]
print(variable)

z = [(x, y) for x in range(3) for y in range(3) if x > y]
print(z)
z = ((x, y) for x in range(3) for y in range(3) if x > y)
print(z)



ddict = {'a': 3, 'd': 8, 'c': 1, 'u': 14}
variable = {key: value for key, value in ddict.items() if value > 5}
print(variable)
del variable['d']
print(variable)
variable = {key: value for key, value in ddict.items() if value > 5}

'''
a = [i for i in range(5)][1:]
print(a)
'''
