import json
from pprint import pprint

filename = 'weather_04_04_2023.json'
with open( filename , 'r') as data:
    jason = json.load(data)
    # pprint(jason)
dayz = []
today_max = 0
today_min = 200
days_temps = {}
doodad = {}
# I need to loop through the list of shit in the 'list' block of this weather data and 
# poops out a dictionary of all the days that follow with an empty list to toss in the
# temperature data
for i in jason['list']:
    # print(type(i))
    splitty = (i['dt_txt']).split(" ")
    if splitty[0] not in dayz:
        dayz.append(splitty[0])
# print(dayz)

for stone,rock in enumerate(dayz):
    days_temps[rock] = []
# loop through the list and assign each dictionary thing to i
for i in jason['list']:
    # now loop through the days in 
    for duck in days_temps.keys():
        doodad[duck] = {}
        doodad[duck].update(i['main'])
        days_temps[duck].append(i['main']['temp'])
    
    
pprint(doodad)     












# pprint(days_temps)
# today_max = max(days_temps)
# today_min = min(days_temps)
# for day in dayz:
#     today_max[day] = 0
#     today_min[day] = 200
    
#     if today_max[day] > i['main']['temp']:
#         today_max[day] = i['main']['temp_max']
#     if today_min[day]> i['main']['temp_min']:
#         today_min[day] = i['main']['temp_min']
    
    
# pprint(today_min)
# print(f'lo {today_min} / high {today_max} ')    
# print(day_1)