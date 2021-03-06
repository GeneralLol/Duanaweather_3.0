'''
This program produces the date and time the main module needs from system time. 
'''
from datetime import datetime

class Time:
    current_time_datetime = datetime.now()
    current_time_str      = ''
    current_time_float    = 0.0
    date = ''
    time = ''
    #Constructor gets everything
    def __init__(self):
        self.current_time_str = str(self.current_time_datetime)
        self.date = self.current_time_str[:10]
        self.time = self.current_time_str[11:]
        self.time =             self.time[:8]
        epoch = datetime.utcfromtimestamp(0)
        self.current_time_float = (self.current_time_datetime - epoch).total_seconds()
    
    def refresh(self):
        self.current_time_datetime = datetime.now()
        self.current_time_str = str(self.current_time_datetime)
        self.date = self.current_time_str[:10]
        self.time = self.current_time_str[11:]
        self.time =             self.time[:8]
        epoch = datetime.utcfromtimestamp(0)
        self.current_time_float = (self.current_time_datetime - epoch).total_seconds()