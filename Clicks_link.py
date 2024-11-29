import requests


token = {'5135fbd85135fbd85135fbd8ed5210bbee551355135fbd8367c2e4ba7a61b6be7bf8da0': '', 'v': 5.199}
response = requests.get('https://api.vk.ru/method/utils.getServerTime', params=token)
response.raise_for_status()

print(response)
print(response.text)
