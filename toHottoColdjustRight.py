from bs4 import BeautifulSoup
from requests import get

url = f"https://www.wunderground.com/weather/us/oh/youngstown"

soup = BeautifulSoup(get(url).text,'html.parser')

temp = int(soup.find(class_ = "wu-unit-temperature").text[:-3])

if temp >= 90:
    print(f"Tempature is too hot")

elif temp < 65:
    print(f"it is too cold")

else:
    print("just perfect weather")