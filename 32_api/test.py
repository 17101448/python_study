import requests
from datetime import datetime 
MY_LAT = 37.6317 
MY_LNG = 127.0775
OPTION = 0 
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": OPTION 
}

response = requests.get("https://api.sunrise-sunset.org/json", verify=False, params=parameters)

response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")
sunset = data["results"]["sunset"].split("T")[1].split(":")

time_now = datetime.now() 


print(sunrise)
print(sunset)
print(time_now.hour)
