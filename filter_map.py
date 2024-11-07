#Пересечение двух массивов

arr1 = ['p','y','t','h','o','n',' ','3','.','0']
arr2 = ['p','y','d','e','v',' ','2','.','0']

out = list(filter(lambda it: it in arr1, arr2))
print(out)

#session = min(filtered_sessions, key=lambda x: abs(datetime.strptime(x.get("startDate"), "%Y-%m-%d") - today))

'''
fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31))

f = lambda x : 1 if x < 2 else x*f(x-1)
print(f(5))

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(map(lambda x: x*2 , current_list))
print(new_list)
'''

def create_tuple(a, b):
    return a, b

# функция `map()` останавливается, когда
# заканчивается самая короткая последовательность
x = map(create_tuple, ['a', 'b'], [3, 4, 5])
print(tuple(x))
x = map(create_tuple, ['a', 'b'], [3, 4, 5])
print(dict(x))
# {'a': 3, 'b': 4}