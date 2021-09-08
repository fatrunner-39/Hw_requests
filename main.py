# Задание 3

import requests

from pprint import pprint
import time


now = round(time.time())
# print(now)
two_days_ago = now - 2*24*3600
# print(two_days_ago)
url = 'https://api.stackexchange.com/2.3/questions'
params = {
    'fromdate': two_days_ago,
    'todate': now,
    'sort': 'creation',
    'order': 'desc',
    'tagged': 'python',
    'site': 'stackoverflow'
}

response = requests.get(url, params=params)
data = response.json()['items']

print('Вопросы за последние 2 дня:')
for question in data:
    print('id:', question['question_id'])
    print('Вопрос:', question['title'])
    print('Ссылка:', question['link'])
    print('Дата:', time.ctime(question['creation_date']))
# pprint(data)
