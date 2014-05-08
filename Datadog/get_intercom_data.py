from intercom import Intercom
import pandas as pd
import requests
import json

Intercom.app_id = 'HIDDEN'
Intercom.api_key = 'HIDDEN'

from intercom import User

base_url = 'https://api.intercom.io/v1'

auth = (app_id, api_key)

users_url = '{0}/users'.format(base_url)


resp = requests.request('GET', users_url, auth=auth)
total_pages = resp.json()['total_pages']
resp_json = resp.json()
resp_dict = resp_json['users']

page = 2
url = '{0}?page={1}'.format(users_url, page)
while page <= total_pages:
    resp = requests.request('GET', url, auth=auth)
    resp_json = resp.json()
    resp_dict = resp_dict + resp_json['users']
    page += 1
    url = '{0}?page={1}'.format(users_url, page)


full_DF = pd.DataFrame(resp_dict)
filteredDF = full_DF[full_DF['session_count'] > 10]
f = open('intercom_users.js','w')
f.write('var intercom_users = ' + filteredDF.reset_index().to_json(orient='records'))
