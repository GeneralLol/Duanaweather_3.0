'''
This module provides the weather class and methods. 
'''
import urllib.request as wreq
import json

class Weather:
    #Independent variables
    city  = ''
    state = ''
    url   = ''
    res   = {}
    obs_rst = ''
    #Dependent variables
    location = ''
    weather  = ''
    temp     = '' # temp as in temperature
    outputStr= '' # The one big string that contains all the info, separated by \n. 
    
    #Constructor. TODO: Have the constructor take city and state from the main module instead of being inputted here. 
    def __init__(self, city, state):
        self.city  = city
        self.state = state
        self.url   = 'http://api.wunderground.com/api/386a8e8ab04d7748/conditions/q/'+self.state+'/'+self.city+'.json'
        self.location = self.city + ' ' + self.state
        
    def check_error(self):
        if ("error" in self.res['response'].keys()):
            #If there is error in the input, return false and raise weatherapiError exception
            raise ValueError('Error fetching information from Weather Underground')
            return False
        else:
            return True
    
    def get_weather(self):
        response_raw = wreq.urlopen(self.url)
        response_str = response_raw.read().decode('utf-8')
        self.res = json.loads(response_str)
        self.check_error() #Make sure the info is correct before proceeding
        
        self.obs_rst = self.res['current_observation']
        self.weather = self.obs_rst['weather']
        self.temp    = str(self.obs_rst['temp_c']) + ' C'
        
        self.outputStr = self.location + '\n' + self.weather + '\n' + self.temp

