num_list = list(i for i in range(10))
print(num_list)


del num_list[4:8]
print(num_list)

'''
new_list = ['ноль', 1, [2.1, 'два и два'], 3, 'IV']
del new_list[2]
print(new_list)

new_list = ['ноль', 1, [2.1, 'два и два'], 3, 'IV']
del new_list[1:4]
print(new_list)
'''


string = "trtrtr/ytyt/ytyt/r"
a = string.split("/")
b = string.strip("/")
print(a)
print(b)
# b = *string.split("/")
def aaa(a,b,c,d):
    return a+b+c+d
print(aaa(*a))
res = [{'rooms': [], "id":25}, {'rooms': [], "id": 7}]

# cabinet_id = [x.get("id") for x in res if len(x.get("rooms")) > 0][0]
# print(cabinet_id)

string = "/api/metrologist/cabinets"
string = string.split("/")
print(string)

day_offs = ['суббота', 'воскресенье']
workdays =['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
weekends = ['пятница','суббота','воскресенье']

res = [*day_offs, *[x for x in weekends if x not in workdays]]
print(res)