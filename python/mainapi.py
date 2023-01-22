import requests

response = requests.get('https://randomuser.me/api')

response_data = response.json()

for user in response_data['results']:
    print(user['name'])
    print('testy')



