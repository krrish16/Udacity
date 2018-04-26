# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:16:17 2018

@author: Krrish
-------------------------TITANIC DATA SET INVESTIGATION---------------------------

Titanic Data - Contains demographics and passenger information from 891 of the 
2224 passengers and crew on board the Titanic.

SOURCE : kaggle

UDACITY COURSE : https://classroom.udacity.com/courses/ud170

To investigate : What factors made people more likely to survive?
                 
Questioning :
    1.What was the range of age group of survived passengers?
    2.Is it true that the women,children and family men were the most likely to survive?
    3.Which class of passengers mostly survived?
    
"""
#%%reading
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv('titanic_data.csv')
print (titanic.head())

print (titanic['Sex'].value_counts())
print ((titanic['Age'] <= 18).value_counts())

#%%child/Adult
def ischild(age):
    if age > 18:
        return "Adult"
    else:
        return "Child"
#ischild(20)
        
titanic["ischild"] = pd.Series(titanic["Age"].apply(ischild), index=titanic.index)


sns.barplot(data=titanic, x="ischild", y="Survived")
plt.show()

#%%
sns.barplot(data=titanic, x="Sex", y="Survived")
plt.show()

"""
From these plots, the probability of survival is much higher in women than in men 
and quite big in children than in adults.In this case it was true that 
women and children first
"""
#%%Age groups

def agegroup(age):
    if age > 0 and age <= 14:
        return "Child"
    if age > 14 and age <= 24:
        return "Youth"
    if age >24 and age <= 64:
        return "Adults"
    else:
        return "Senior"

titanic["AgeGroup"] = pd.Series(titanic["Age"].apply(agegroup), index=titanic.index)

sns.barplot(data=titanic, x="AgeGroup", y="Survived")

"""
From the plots, it is observed that the age group of 0-14 (i.e, childern) were having
high probability of survival then the youth and adults
"""
#%%have_family?

def relationship(data):
    if data["SibSp"] > 0:
        if data["Parch"] > 0:
            return "Father"
        else:
            return "Husband"
    else:
        return "Single"
    

def isAdult(x):
    return x["ischild"] == "Adult" and x["Sex"] == "male"

adult_titanic = titanic[titanic.apply(isAdult, axis=1)]
    
adult_titanic["FamilyMan"] = pd.Series(adult_titanic.apply(relationship, axis=1), index=adult_titanic.index)

print (adult_titanic["FamilyMan"].value_counts())

sns.factorplot(data=adult_titanic,x="Survived", col="FamilyMan", kind="count")


#%%Class
sns.barplot(data=adult_titanic, x="Pclass" , y="Survived")

#%%
sns.barplot(data=titanic, x="Sex", y="Survived",hue ="Pclass")

"""
It is clear that the First class passengers had more chances of survive than 
second class and third class.

And considering overall survival probability it is observed to be high in female 
compared to male
"""
#%%
"""
Conclusions: 
Let us conduct a hypothesis test to see if there is a significant difference 
between proportions. 
(i) male and female
(ii) Adults and children

H0 : P1 − P2 = 0
HA : P1 − P2 ≠ 0

Conducting Two-proportion z-test

Pooled sample proportion: p = (p1 ∗ n1) + (p2 * n2) / n1 + n2
Standard error: SE = sqrt( p ∗ (1 − p) ∗ ((1/n1) +(1/n2)) )
Test statistic: z =p1 − p2/SE

"""
import math

male = titanic[titanic["Sex"]== "male"]
female = titanic[titanic["Sex"]== "female"]
total_people = len(male) + len(female)

pmale = float(len(male[male["Survived"] == 1])) / len(male)
pfemale = float(len(female[female["Survived"] == 1])) / len(female)
p = (pmale * len(male) + pfemale * len(female)) / total_people
print ("p :", p)
SE = math.sqrt(p * ( 1 - p ) * ( float(1)/len(male) + float(1)/len(female) ))
print ("SE : ", SE)
z = (pmale - pfemale) / SE
print ("z :", z)

child = titanic[titanic["Age"] <= 18]
adult = titanic[titanic["ischild"]== "Adult"]

pchild = float(len(child[child["Survived"] == 1])) / len(child)
padult = float(len(adult[adult["Survived"] == 1])) / len(adult)
p = (pchild * len(child) + padult * len(adult)) / total_people
print ("p :", p)
SE = math.sqrt(p * ( 1 - p ) * ( float(1)/len(child) + float(1)/len(adult) ))
print ("SE : ", SE)
z = (pchild - padult) / SE
print ("z :", z)
"""
(i)The P-value is going to be very very small (smaller than our significance level 0.05). 
So we can consider reject the null hypothesis and say that in this scenario there 
is a significant difference between proportions.

(ii)The P-value for P(z > 2.606) = 0.0039 in a two-tailed test is 0.0039 + 0.0039. 
So P-value = 0.0078, smaller than 0.05 and again the difference between proportions
are significant.
"""
#%%


