import requests
from collections import Iterable, Iterator
# 气温迭代器
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
    def getWeather(self, city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s：%s , %s' % (city, data['low'], data['high'])
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)
# 可迭代对象
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)
for x in WeatherIterable(['北京', '上海', '广州', '深圳']):
    print(x)