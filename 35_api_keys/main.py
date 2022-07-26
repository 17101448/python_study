import requests 

from twilio.rest import Client 


api_keys = "4ba30de297a5cd3090a995ed997a8fe1"
MY_LAT = 37.6317 # Your latitude
MY_LONG = 127.0775 # Your longitude

account_sid = "AC6762672c74ebf1d3c0eb22e9c911e6c1"
auth_token = "89aeea085a6eb20d4627554afdfa5b3a"


parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : api_keys,
    "exclude" : "current, minutely, daily",
    "units" : "metric"
}

response = requests.get(url= "https://api.openweathermap.org/data/2.5/onecall", params = parameters)

response.raise_for_status() 

data = response.json() 

will_rain = False 
weather_list = [] 
#print(data["hourly"])
for hour_data in data["hourly"][:12]:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True 

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="12시간 내에 비가 올 예정이니 우산을 챙기세요",
                     from_='+18434387890',
                     to="+821025722860"
                 )
    print(message.status)

