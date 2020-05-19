import requests
import json

lode_typ = list()
lode_id = list()

request = requests.get('https://api.spacexdata.com/v3/launches/past', 
    params={'rocket_id': 'falcon9', 'launch_success': 'false'}
    ).json()

for req in request:
    if req['launch_year'] == '2015':
        lode_id.append(req['ships'])

for id in lode_id:
    req = requests.get('https://api.spacexdata.com/v3/ships/{}'.format(id)).json()
    lode_typ.append(req['ship_type'])

print(lode_typ)