# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:25:15 2018

@author: Krrish
"""

#%%
import pandas as pd
employ = pd.read_csv('employment_above_15.csv')
female = pd.read_csv('female_completion_rate.csv')
gdp = pd.read_csv('gdp_per_capita.csv')
male = pd.read_csv('male_completion_rate.csv')
life = pd.read_csv('life_expectancy.csv')


#%%max emplyment country and value
import numpy as np
# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

def max_employment(countries , employment):
    i = employment.argmax()
    max_country = countries[i]
    max_value = employment[i]
    return (max_country , max_value)

max_coun = max_employment(countries , employment)

print (max_coun)

#%% 
    
for i in range(len(countries)):
    print ('Country {} has employment {}'.format(countries[i] , employment[i]))

 #%%overall completion rate
import numpy as np
female_completion = np.array([
    97.35583,  104.62379,  103.02998,   95.14321,  103.69019,
    98.49185,  100.88828,   95.43974,   92.11484,   91.54804,
    95.98029,   98.22902,   96.12179,  119.28105,   97.84627,
    29.07386,   38.41644,   90.70509,   51.7478 ,   95.45072
])

# Male school completion rate in 2007 for those 20 countries
male_completion = np.array([
     95.47622,  100.66476,   99.7926 ,   91.48936,  103.22096,
     97.80458,  103.81398,   88.11736,   93.55611,   87.76347,
    102.45714,   98.73953,   92.22388,  115.3892 ,   98.70502,
     37.00692,   45.39401,   91.22084,   62.42028,   90.66958
])
    
def overall_completion_rate(female_completion , male_completion):
    return (female_completion + male_completion) / 2
    

#%%standardizing data
def standardize_data(values):
    sd = np.array((values - values.mean())/values.std())
    return sd

output = standardize_data(employment)
print (output)
#%%NumPy Index Arrays

time_spent = np.array([
       12.89697233,    0.        ,   64.55043217,    0.        ,
       24.2315615 ,   39.991625  ,    0.        ,    0.        ,
      147.20683783,    0.        ,    0.        ,    0.        ,
       45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
        0.        ,   54.9204785 ,   26.78142417,    0.
])

# Days to cancel for 20 students
days_to_cancel = np.array([
      4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
     38,  98,   2, 249,   2, 127,  35
])
    

def mean_time_paid(time_spent, days_to_cancel):
    return time_spent[days_to_cancel >= 7].mean()

mean_time = mean_time_paid(time_spent, days_to_cancel)
print (mean_time)

    
#%%Panda Series
import pandas as pd
life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]

life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)

def variable_correlation(variable1,variable2):
    above = (variable1 > variable1.mean()) & (variable2 > variable2.mean())
    below = (variable1 < variable1.mean()) & (variable2 < variable2.mean())
    same_dir = above | below
    num_same_dir = same_dir.sum()
    num_diff_dir = len(variable1) - num_same_dir
    return (num_same_dir , num_diff_dir)

variable_correlation(life_expectancy , gdp)
#%%series indexes
import pandas as pd

countries1 = [
    'Afghanistan', 'Albania', 'Algeria', 'Angola',
    'Argentina', 'Armenia', 'Australia', 'Austria',
    'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
    'Barbados', 'Belarus', 'Belgium', 'Belize',
    'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
]


employment_values1 = [
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076,
]

# Employment data in 2007 for 20 countries
employment = pd.Series(employment_values1, index=countries1)

def max_employment(employment):
    max_country = employment.idxmax()
    max_value = employment.max()
    return (max_country, max_value)

maxi = max_employment(employment)
print (maxi)

#%%reverse names

names_reverse = pd.Series([
    'Andre Agassi',
    'Barry Bonds',
    'Christopher Columbus',
    'Daniel Defoe',
    'Emilio Estevez',
    'Fred Flintstone',
    'Greta Garbo',
    'Humbert Humbert',
    'Ivan Ilych',
    'James Joyce',
    'Keira Knightley',
    'Lois Lane',
    'Mike Myers',
    'Nick Nolte',
    'Ozzy Osbourne',
    'Pablo Picasso',
    'Quirinus Quirrell',
    'Rachael Ray',
    'Susan Sarandon',
    'Tina Turner',
    'Ugueth Urbina',
    'Vince Vaughn',
    'Woodrow Wilson',
    'Yoji Yamada',
    'Zinedine Zidane'
])

def reverse_names(names):
    spliting = names.split(" ")
    first_name = spliting[0]
    last_name = spliting[1]
    return last_name+', '+first_name

def reversed_name(names):
    return names_reverse. (reverse_names)

rever = reversed_name(names_reverse)
print (rever)
#%%