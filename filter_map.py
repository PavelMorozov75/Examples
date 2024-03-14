#Пересечение двух массивов

arr1 = ['p','y','t','h','o','n',' ','3','.','0']
arr2 = ['p','y','d','e','v',' ','2','.','0']

out = list(filter(lambda it: it in arr1, arr2))
print(out)

#session = min(filtered_sessions, key=lambda x: abs(datetime.strptime(x.get("startDate"), "%Y-%m-%d") - today))