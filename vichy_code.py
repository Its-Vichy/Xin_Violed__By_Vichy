import requests, json
for item, key in (requests.get('https://discord.com/api/v6/users/@me', headers= {'Authorization': input('Token: '), 'content-type': 'application/json'}).json()).items():
    print(f'{item}: {key}')