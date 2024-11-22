import requests


def get_weather(*args):
    weather_cities = ''
    for location in args:
        url = f'https://wttr.in/{location}?M?nTqu&lang=ru'
        response = requests.get(url)
        response.raise_for_status()
        weather_cities += response.text

    return weather_cities


if __name__ == '__main__':
    print(get_weather('london', 'SVO', 'Череповец'))

