from __future__ import print_function
import pickle
import os.path
from datetime import datetime 
from datetime import date 
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = 'REDACTED'
SAMPLE_RANGE_NAME = 'A2:B'

def DailyAvgCubeTime():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    result = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    rows = result.get('values')
    #print(rows)


    #get today
    today = date.today()
    today = today.strftime("%m/%d/%Y")

    print(today)

    #define times list
    dailyTimes = []
    count = 0

    for i in rows:
        for p in i:
            count = count + 1
            if(p == today):
                #get time of matched date
                dailyTimes.append(i[1])
                #print(p)

    print(dailyTimes)

    lengthOfList = len(dailyTimes)
    if lengthOfList <=0:
        dailyAvg= "There have been no cubes today."
        return dailyAvg

    totalSecs = 0

    #calculate average
    #for dt in dailyTimes:
       # dailyTotal = dailyTotal + dt
        #at = datetime.strptime(dt, "%H:%M:%S")
        #dailyTotal = dailyTotal + time.mktime(at.timetuple())

    for tm in dailyTimes:
        timeParts = [int(s) for s in tm.split(':')]
        totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
    
    #get Avg
    totalSecs = totalSecs/lengthOfList
    totalSecs, sec = divmod(totalSecs, 60)
    hr, min = divmod(totalSecs, 60)
    dailyAvg = "%d:%02d:%02d" % (hr, min, sec)

    print(dailyAvg)

    return dailyAvg



if __name__ == '__main__':
    DailyAvgCubeTime(today)