import requests


if __name__ == '__main__':
    params = {'MnqT': '', 'lang': 'ru'}
    cities = [
        'london',
        'SVO',
        'Череповец',
    ]

    for city in cities:
        response = requests.get(f'https://wttr.in/{city}', params=params)
        response.raise_for_status()
        print(response.text)


