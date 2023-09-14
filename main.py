import datetime

import requests

YOUR_API_KEY = 'YOUR_API_KEY'  # enter your API key here


def check_api_key():
    if YOUR_API_KEY == 'YOUR_API_KEY':
        raise Exception('You did not specify the wakatime API key.')
    else:
        return YOUR_API_KEY


def check_response(response):
    if response.get('error'):
        raise Exception(response['error'])
    else:
        return response


def get_response(url, params):
    response = check_response(requests.get(url, params=params).json())
    return response


fts = datetime.datetime.fromtimestamp
today = datetime.datetime.now().strftime('%Y-%m-%d')
API_KEY = check_api_key()


def get_last_session():
    """
    Выводит последнюю сессию
    Template (первый сигнал(%H:%M) - последний сигнал(%H:%M) | продолжительность(%H:%M:%s)
    """
    url = 'https://wakatime.com/api/v1/users/current/durations'
    params = {
        'api_key': API_KEY,
        'date': today,
    }

    response = get_response(url, params)['data'][-1]

    start_session = fts(response['time']).strftime('%H:%M')
    duration = datetime.timedelta(seconds=int(response['duration']))
    end_session = fts(response['time'] + response['duration']).strftime('%H:%M')

    print(f'{start_session} - {end_session} | {duration}')


def get_time_for_today():
    """
    Выводит статистику за день
    Example 1 hr 18 mins
    """
    url = 'https://api.wakatime.com/api/v1/users/current/summaries'
    params = {
        'api_key': API_KEY,
        'start': today,
        'end': today
    }

    response = get_response(url, params)

    print(response['data'][0]['grand_total']['text'])


if __name__ == '__main__':
    get_last_session()
    get_time_for_today()
