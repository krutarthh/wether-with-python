import requests
from pprint import pprint
API="6ce6a271361aaff5e75e123b93335943"
city=input('enter city:')
base=f'https://api.openweathermap.org/data/2.5/weather?q={city.lower()}&appid={API}'
weather=requests.get(base).json()
pprint(weather)

