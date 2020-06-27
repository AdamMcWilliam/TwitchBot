import json
from datetime import datetime 
from datetime import date 
import time

newData = {}
newData['cubed'] = []

with open('user_events.txt') as json_file:
    data = json.load(json_file)
    for i in data['user_events']:
    #print(data['user_events'][f'{i}']['msg'])
        if data['user_events'][f'{i}']['command'] == "cubed":
            newData['cubed'].append({
                "user": data['user_events'][f'{i}']['user'],
                "command": data['user_events'][f'{i}']['command'],
                "msg": data['user_events'][f'{i}']['msg'],
                "result": data['user_events'][f'{i}']['result'],
                "created_at": data['user_events'][f'{i}']['created_at']
                })
         
with open('cubed.txt', 'w') as outfile:
    json.dump(newData, outfile)