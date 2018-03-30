# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 17:34:07 2018

@author: Krrish
"""

#%%ridership

import numpy as np

# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])

def mean_riders_for_max_station(ridership):
    first_day_max_station = ridership[0,:].argmax()
    mean_rider_that_station = ridership[:,first_day_max_station].mean()
    overall_mean = ridership.mean()
    return (first_day_max_station,mean_rider_that_station,overall_mean)

ans = mean_riders_for_max_station(ridership)
print (ans)

#%%max min riders

def min_and_max_riders_per_day(ridership):
    max_daily_ridership = ridership.mean(axis=0).max()
    min_daily_ridership = ridership.mean(axis=0).min()
    return (max_daily_ridership, min_daily_ridership)

ans2 = min_and_max_riders_per_day(ridership)
print (ans2)
#%%Data Frames

import pandas as pd

# Subway ridership for 5 stations on 10 different days
ridership_df = pd.DataFrame(
    data=[[   0,    0,    2,    5,    0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [  95,  229,  255,  496,  201],
          [   2,    0,    1,   27,    0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)

def mean_riders_for_max_station_df(ridership):
    first_day_max = ridership_df.iloc[0].idxmax()
    overall_mean = ridership_df.values.mean() # Replace this with your code
    mean_for_max = ridership_df[first_day_max].values.mean() # Replace this with your code
    return (overall_mean, mean_for_max)
    
ans = mean_riders_for_max_station_df(ridership_df)
print (ans)
    

#%%loading data to dataframe

import pandas as pd
subway_df = pd.read_csv('nyc_subway_weather.csv')

subway_df.head()  #give first 5 data lines
subway_df.describe()

#%%  

