from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

class Calendar:
    events= None
    events_result = None
    blocks = []
    refresh_time = None
    next_block = ''
    #Constructor. 
    #Setting up for the Google Calendar, and getting the raw, unprocessed events. 
    def __init__(self):
        secret_dir = 'secret.json'
        credentials_dir = 'credentials.json'
        
        SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
        store = file.Storage(credentials_dir)
        creds = store.get()
    
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(secret_dir, SCOPES)
            creds = tools.run_flow(flow, store)
            creds = tools.run_flow(flow, store)
        
        service = build('calendar', 'v3', http=creds.authorize(Http()))
    
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        calendarid = 'i7vs7cuh27t4kvh0k517tnk3m8fjms11@import.calendar.google.com'
        self.events_result = service.events().list(calendarId=calendarid, timeMin=now,
                                              maxResults=60, singleEvents=True,
                                              orderBy='startTime').execute()
                                    
        self.events = self.events_result.get('items', [])
    
    
        if not self.events:
            raise ValueError("No upcoming events.")
    
    def get_upcoming_event(self):
        index = 0
        refresh_index = 0
        start = [None] * 60
        refresh_flag = False
        refresh_counter = True
        for event in self.events:
            start[index] = event['start'].get('dateTime', event['start'].get('date'))
            #If there are 20 chars in start, it's a class. Otherwise it's a homework.
            if len(start[index]) == 20:
                self.blocks.append(event['summary'])
                refresh_flag = True
            if refresh_flag and refresh_counter:
                refresh_index = index
                refresh_counter = False
            index += 1
        self.blocks.pop(0)
        
        flag = False
        for i in self.blocks[1]:
            if i == '(':
                flag = True
            if i == ')':
                pass
            if flag:
                self.next_block += i
        length = len(self.next_block)
        self.next_block = self.next_block[1:]
        self.next_block = self.next_block[:length-2]
        
        #Get the time for next refresh\
        try: 
            utc_time = datetime.datetime.strptime(start[refresh_index+1], "%Y-%m-%dT%H:%M:%SZ")
            epoch = datetime.datetime.utcfromtimestamp(0)
            self.refresh_time = (utc_time-epoch).total_seconds()
        except:
            print("Unable to retreive proper refresh time.")
        