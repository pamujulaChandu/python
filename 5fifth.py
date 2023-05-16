# Using REQUESTS lib and dictionary and feltching the data from the internet (json data)
import requests

people=requests.get('http://api.open-notify.org/astros.json')

json= people.json()

print(json)

for i in json['people']:
    print(i['craft'])

