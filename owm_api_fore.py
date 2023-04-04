import requests
import json
from datetime import datetime
import os


now = datetime.now()
current = now.strftime("%d_%m_%Y")
with open(f'weather_{current}.json', 'w') as weather:
  params = {
    'units': 'imperial'
  }
  api_key = '167963164c70cf7e7b887ac578ba9a58'
  lat = 35.053
  lon = -78.879
  api_result = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}', params)
  api_response = api_result.json()
  # for k, v in api_response.items():
  #     print(v)
  # print(type(api_response))

  # for k, v in api_response.items():
  #     print(v[dt])
  py_response = json.dumps(api_response, indent=4)
  weather.write(py_response)
print(current)
