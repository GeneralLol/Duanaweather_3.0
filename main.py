'''
This is the main module for Duanaweather 3.0. 
Duanaweather 3.0 is an object-oriented implementation of the original Duanaweather application. 
'''
import sys
import m_weather
import m_time
import m_calendar
from time import sleep

def main():
    #Input the city and state (TODO: work it into sys.argv)
    city  = input ("Please input name of city:  \n>")
    state = input ("Please input name of state: \n>")
    weather = m_weather.Weather(city, state)
    time    = m_time.Time()
    calendar= m_calendar.Calendar()
    #Pull info from m_weather object
    try:
        weather.get_weather()
        calendar.get_upcoming_event()
    except ValueError as msg:
        print (msg)
        sys.exit()

    while (True): 
        if (calendar.refresh_time <= time.current_time_float):
            calendar.refresh()
            
        time.refresh()
        print(weather.weather)
        print(weather.temp)
        print(weather.location)
        print(time.date)
        print(time.time)
        print(calendar.next_block)
        print(calendar.refresh_time)
        sleep(1)

if (__name__ == "__main__"):
    main()
