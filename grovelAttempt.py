import json
from datetime import datetime 
from datetime import date 
import time

def grovelAttempt(author):

    #get today
    today = date.today()
    today = today.strftime("%m/%d/%Y")
    
    grovellCount = 0
    #check file for previous attempts
    with open('grovellers.txt') as json_file:
        data = json.load(json_file)
        for g in data['grovelers']:
            if g['name'] == author and g['date'] == today:
                grovellCount +=1


    #add attempt to file
    #data = {}
    #data['grovelers'] = []
    data['grovelers'].append({
        'name': author,
        'date': today
    })


    with open('grovellers.txt', 'w') as outfile:
        json.dump(data, outfile)

    #return message based on number of grovels
    msg1 = f"I don't know... @{author}"
    msg2  = f"!props @{author} fine..."
    msg3 = f"@{author} you've had enough peasant!"

    if grovellCount <= 1:
        return msg1
    elif grovellCount == 2:
        return msg2
    else:
        return msg3
       
