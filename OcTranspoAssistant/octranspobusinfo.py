import requests
import json
import urllib.parse
busInfo = input("Bus: ")
stopInfo = input("Stop No: ")
data = {
  'appID': 'aaff9a58',
  'apiKey': 'ca96a92860ca65420c73e292659192c5',
  'routeNo': busInfo,
  'stopNo': stopInfo,
  'format': 'json'
}

response = requests.post('https://api.octranspo1.com/v1.2/GetNextTripsForStop', data=data)
responseData = response.json()
for each in responseData['GetNextTripsForStopResult']['Route']['RouteDirection']['Trips']['Trip']:
    int3 = each['TripStartTime']
    print(int3)
    int2 = each['AdjustedScheduleTime']
    float2 = float(int2)
    print(float2)
    int1 = each['AdjustmentAge']
    float1 = float(int1)
    if float1 > 0:
        print(float1)
