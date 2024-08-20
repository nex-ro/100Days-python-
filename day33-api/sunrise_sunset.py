import requests
myLat=0.502134
myLong=101.454010

parameter={
    "lat":myLat,
    "lng":myLong,
    "formatted":1
}
response=requests.get("https://api.sunrisesunset.io/json",params=parameter)
response.raise_for_status()
data=response.json()
print(data)