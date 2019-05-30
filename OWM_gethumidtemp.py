#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:20:08 2019

@author: knut

Simple script to retrieve weather data from the OpenWeatherMap API. Currently retrieves temperature, humidity, city and time info, 
but could easily be adjusted to get other measurements. Currently only prints the dataframe, but could easily be adjusted to save it
or append new rows to an existing dataframe.)
"""

import requests, re
import pandas as pd

def get_temp_humidity(cities):
    """
    Get temperature and humidity information from OpenWeatherMap.
    
    Args:
        cities: List of OWM city ID-numbers
    
    Returns:
        Pandas Dataframe with (local) time, city name, country code, humidity level and temperature for cities
        
    Example function call:
        get_temp_humidity([3143244,1733046,1819729,1809858,1804651,1886760,1668341])
    """
    data_list = []
    for city_ID in cities:
        weather_dict = {}    
        api_address = 'https://api.openweathermap.org/data/2.5/weather?appid='
        api_key = 'YOU-API-KEY-GOES-HERE' #replace text with your api-key
        city = '&id='+str(city_ID)
        metric = '&units=metric' #to get temperature in Celcius, as the default value returned by the API is in Kalvin
    
        url = api_address + api_key + city + metric
        json_data = requests.get(url).json()
        
        data_time_local = str(pd.to_datetime(json_data['dt']+json_data['timezone'], unit='s'))
        time_split = re.split('-|\s', data_time_local)
        
        weather_dict['city_name'] = json_data['name']
        weather_dict['country_code'] = json_data['sys']['country']
        weather_dict['humidity'] = json_data['main']['humidity']
        weather_dict['temperature'] = json_data['main']['temp']
        weather_dict['year'] = time_split[0]
        weather_dict['month'] = time_split[1]
        weather_dict['day'] = time_split[2]
        weather_dict['time'] = time_split[3]
        
        
        data_list.append(weather_dict)
    df = pd.DataFrame(data_list)
    print(df)
    
