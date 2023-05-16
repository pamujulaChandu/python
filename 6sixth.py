import requests
api_key='c4ea208e187f54254ebe0cd94d3ce263'
city="Orlando"
url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
request=requests.get(url)
json=request.json()
print(json)

#it is not working