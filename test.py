from naverWeather import *
l = naverWeather.map_cityNum.keys()
for s in l :
    print(s)
    print(naverWeather(s).getWeather())
