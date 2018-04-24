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
    first_day_max = ridership_df.loc['05-01-11'].idxmax()
    overall_mean = ridership_df.values.mean() # Replace this with your code
    mean_for_max = ridership_df[first_day_max].values.mean() # Replace this with your code
    return (first_day_max,overall_mean, mean_for_max)
    
ans = mean_riders_for_max_station_df(ridership_df)
print (ans)
    

#%%loading data to dataframe

import pandas as pd
subway_df = pd.read_csv('nyc_subway_weather.csv')

subway_df.head()  #give first 5 data lines
subway_df.describe()
#%%
df = pd.DataFrame({'A':[1,2,3],'B':[3,4,5]})
print (df)

#%%correlation-standardizing

#correlation = avg of (x in std) times (y in std)

def correlation(x,y):
    stdx = (x-x.mean())/x.std(ddof=0)
    stdy = (y-y.mean())/y.std(ddof=0)
    return ((stdx*stdy).mean())

##SIMPLY USE = corrcoef() for correlation

#%%Vectorised operations
import pandas as pd

entries_and_exits = pd.DataFrame({
    'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                 3144808, 3144895, 3144905, 3144941, 3145094],
    'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
               1088317, 1088328, 1088331, 1088420, 1088753]
})
    
def get_hourly_entries_and_exits(entries_and_exits):
    print (entries_and_exits.diff())

get_hourly_entries_and_exits(entries_and_exits)

#%%applymap()

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James'])
    
def convert_grade(grades):
    if grades >= 90:
        return 'A'
    elif grades >=80:
        return 'B'
    elif grades >= 70:
        return 'C'
    elif grades >= 60:
        return 'D'
    else:
        return 'F'
    
def convert_grades(grades):
    print (grades_df.applymap(convert_grade))
    
convert_grades(grades_df)

#%%applymap2
import pandas as pd
df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})
 
def secmax(column):
    sorted_secmax = column.sort_values(ascending=False)
    return sorted_secmax.iloc[1]
def second_largest(df):
    return df.apply(secmax)

print (second_largest(df))

#%%dataframe + series

#%%Standardizing

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

#standadizing column
# grades_df.mean()
# (grades_df - grades_df.mean())/gades_df.std()

#stabdadizing row
#  grades_df.mean(axis = 1)
#  mean_diff = grades_df.sub(grades_df.mean(axis = 'columns'),axis='index'
#  mean_diff.div(grades_df.std(axis = 'columns'),axis = 'index')

#%%GroupBy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
subway_df = pd.read_csv('nyc_subway_weather.csv')

print (subway_df.head())

grouped = subway_df.groupby('rain')
raingroup =  (grouped.mean()['ENTRIESn'])
print (raingroup)

grouped1 = subway_df.groupby('day_week')
daygroup = (grouped.mean()['ENTRIESn'])
print (daygroup)

%pylab inline
import seaborn as sns
raingroup.plot()
daygroup.plot()

#%%

ridership_df = pd.DataFrame({
    'UNIT': ['R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051'],
    'TIMEn': ['00:00:00', '02:00:00', '04:00:00', '06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00'],
    'ENTRIESn': [3144312, 8936644, 3144335, 8936658, 3144353, 8936687, 3144424, 8936819, 3144594],
    'EXITSn': [1088151, 13755385,  1088159, 13755393,  1088177, 13755598, 1088231, 13756191,  1088275]
})

entries_and_exits = pd.DataFrame({
    'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                 3144808, 3144895, 3144905, 3144941, 3145094],
    'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
               1088317, 1088328, 1088331, 1088420, 1088753]
})

def per_hour(entries_and_exit):
    return entries_and_exits - entries_and_exits.shift(1)
    
    
hourgroup = ridership_df.groupby('UNIT').apply(per_hour)
print (hourgroup)

#%%

