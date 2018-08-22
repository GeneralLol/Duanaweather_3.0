'''
This is the main module for Duanaweather 3.0. 
Duanaweather 3.0 is an object-oriented implementation of the original Duanaweather application. 
'''
import sys
import m_weather
import m_time
import m_calendar

def main():
    #instance the m_weather class
    #TODO: Have the city and state inputed here instead of the class constructor
    weather = m_weather.Weather()
    time    = m_time.Time()
    calendar= m_calendar.Calendar()
    #Pull info from m_weather object
    try:
        weather.get_weather()
        calendar.get_upcoming_event()
    except ValueError as msg:
        print (msg)
        sys.exit()

    print(weather.weather)
    print(weather.temp)
    print(weather.location)
    print(time.date)
    print(time.time)
    print(calendar.next_block)
    print(calendar.refresh_time)
    

if (__name__ == "__main__"):
    main()