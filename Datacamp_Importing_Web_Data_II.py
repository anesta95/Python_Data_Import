import json
import requests
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'
r = requests.get(url)
print(r.text)
json_data = r.json()
for k in json_data.keys():
    print(k + ":", json_data[k])

url1 = 'https://en.wikipedia.org/w/api.php?action=query&\
prop=extracts&format=json&exintro=&titles=pizza'

rq = requests.get(url1)
json_data1 = rq.json()
pizza_extract = json_data1['query']['pages']['24768']['extract']
print(pizza_extract)
