import datetime

import requests

API_KEY = 'YOUR_API_KEY'  # enter your API key here

if API_KEY == 'YOUR_API_KEY':
    raise Exception('You did not specify the wakatime API key.')

url = 'https://api.wakatime.com/api/v1/users/current/summaries'

today = datetime.datetime.now().strftime('%Y-%m-%d')

params = {
    'api_key': API_KEY,
    'start': today,
    'end': today
}

response = requests.get(url, params=params).json()

if response.get('error'):
    raise Exception(response['error'])
print(response['data'][0]['grand_total']['text'])
