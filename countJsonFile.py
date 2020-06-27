import json
from datetime import datetime 
from datetime import date 
import time

with open('theives.txt') as json_file:
    data = json.load(json_file)
    print len(data['theives'][1]['user'])