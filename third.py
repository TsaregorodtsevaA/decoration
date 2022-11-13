import requests
from pprint import pprint
from  first import logger
url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
all = response.json()
@logger
def the_most_intelligence(*args):
    intelligence = []
    for person in args:
        for el in all:
            if person ==el['name']:
                intelligence.append(el["powerstats"]['intelligence'])
                max_int = sorted(intelligence)
    for person in args:
        for i in all:
            if person == i['name']:
                if max_int[-1]== i["powerstats"]['intelligence']:
                    return person

print(the_most_intelligence('Captain America', 'Hulk', 'Thanos'))