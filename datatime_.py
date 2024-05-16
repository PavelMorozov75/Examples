import time
from datetime import datetime


# Assuming supply_date is a datetime object
supply_date = datetime.now()
print(supply_date)

# Format the datetime object into a string with microseconds truncated to three decimal places
supply_date_str = supply_date.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

print(supply_date_str)

sorting_start_date = datetime.today().replace(day=1)
print(sorting_start_date.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

'''
d = time.time()
print(d)
a = datetime.fromtimestamp(d/ 1000).strftime('%d-%m-%Y %H:%M:%S.%f')
print(a)
print(type(a))
'''

'''
import json
from datetime import datetime
sorting_start_date = datetime.today().replace(day=1)
sorting_close_date = datetime.today()
sorting_result = {
            "CloseDate": sorting_close_date.strftime("%Y-%m-%dT%H:%M:%S"),
            "StartDate": sorting_start_date.strftime("%Y-%m-%dT%H:%M:%S"),
            "TotalWeight": 0,
            "WeightByTask": {}

        }
print(sorting_result)
print(str(sorting_result))
sorting_result1 = str(sorting_result).replace("'", '"')
sorting_result2 = json.dumps(sorting_result)
print(sorting_result1)
print(sorting_result2)
'''

'''
import datetime as dt
j, m, d = map(int, input().split())
int_delta= int(input())
new_date = dt.datetime(j,m,d)+dt.timedelta(days=int_delta)
print (int(new_date.strftime('%Y')), int(new_date.strftime('%m')), int((new_date.strftime('%d'))))
print(j, m, d)
print(int_delta)
'''