'''
This is the main module for Duanaweather 3.0. 
Duanaweather 3.0 is an object-oriented implementation of the original Duanaweather application. 
'''
import sys
import m_weather

def main():
    #instance the m_weather class
    #TODO: Have the city and state inputed here instead of the class constructor
    weather = m_weather.Weather()
    #Pull info from m_weather object
    try:
        weather.getWeather()
    except ValueError as msg:
        print (msg)
        sys.exit()
        
    print(weather.m_weather)
    print(weather.temp)
    print(weather.location)

if (__name__ == "__main__"):
    main()