import requests

def getWeather():
    """
        获取天气的地址有问题
    """
    r = requests.get('http://www.weather.com.cn/data/sk/101020100.html')
    r.encoding = 'utf-8'
    data = r.json()['weatherinfo']
    city = data['city']
    WD = data['WD']
    temp = data['temp']
    return city, WD, temp

if __name__ == '__main__':
    city, WD, temp = getWeather()
    print(f"城市: {city}")
    print(f"风向: {WD}")
    print(f"温度: {temp}℃")