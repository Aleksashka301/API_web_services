import requests


if __name__ == '__main__':
    headers = {'Accept-Language': 'ru-RU'}
    params = {'MqT&lang=ru': ''}
    cities = [
        'london',
        'SVO',
        'Череповец',
    ]
    weather_cities = ''

    for city in cities:
        response = requests.get(f'https://wttr.in/{city}', params=params, headers=headers)
        response.raise_for_status()
        weather_cities += response.text

    print(weather_cities)
