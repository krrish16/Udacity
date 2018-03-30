# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#%%Opening file

import unicodecsv
def open_file(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enroll = open_file('enrollments.csv')
engage = open_file('daily_engagement.csv')
submi = open_file('project_submissions.csv')
#%%

#%%fixing data types

from datetime import datetime as dt
def fix_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date,'%Y-%m-%d')

def to_int(i):
    if i == '':
        return None
    else:
        return int(i)

for e in enroll:
    e['cancel_date'] = fix_date(e['cancel_date'])
    e['days_to_cancel'] = to_int(e['days_to_cancel'])
    e['is_canceled'] = e['is_canceled'] == 'True'
    e['is_udacity'] = e['is_udacity'] == 'True'
    e['join_date'] = fix_date(e['join_date'])

for e in engage:
    e['lessons_completed'] = int(float(e['lessons_completed']))
    e['num_courses_visited'] = int(float(e['num_courses_visited']))
    e['projects_completed'] = int(float(e['projects_completed']))
    e['total_minutes_visited'] = float(e['total_minutes_visited'])
    e['utc_date'] = fix_date(e['utc_date'])
    
for s in submi:
    s['completion_date'] = fix_date(s['completion_date'])
    s['creation_date'] = fix_date(s['creation_date'])
#%%
    
#%%Investigating data
#fixing engagement key
for e in engage:
    e['account_key'] = e['acct']
    del (e['acct'])

print (len(enroll))    
unienroll = set()
for e in enroll:
    unienroll.add(e['account_key'])
print (len(unienroll))

print (len(engage))
uniengage = set()
for e in engage:
    uniengage.add(e['account_key'])
print (len(uniengage))

print (len(submi))
unisubmi = set()
for e in submi:
    unisubmi.add(e['account_key'])
print (len(unisubmi))    
#%%    

#%%Missing Records

for e in enroll:
    if e['account_key'] not in uniengage:
        print (e)

#%%
        
#%%remove udacity acc
        
udacity_acc = set()
for e in enroll:
    if e['is_udacity']:
        udacity_acc.add(e['account_key'])
len(udacity_acc)        

def non_udacity(given):
    non_udacity = []
    for i in given:
        if i['account_key'] not in udacity_acc:
            non_udacity.append(i)
    return non_udacity
#%%

#%%Refinig ques

paid_students = {}
for i in non_udacity(enroll):
    key = i['account_key']
    value = i['join_date']
    if not i['is_canceled'] or i['days_to_cancel'] > 7:
        if key not in paid_students or paid_students[key] > value:
            paid_students[key] = value 
len(paid_students)
#%%

#%%OneWeek and Remove free trial acc

def oneweek(join_date,engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7 and time_delta.days > 0

def removetrail(data):
    new = []
    for p in data:
        if p['account_key'] in paid_students:
            new.append(p)
    return new

paid_enroll = removetrail(non_udacity(enroll))
paid_engage = removetrail(non_udacity(engage))
paid_submi = removetrail(non_udacity(submi))
#%%
print (len(paid_enroll))
print (len(paid_engage))
print (len(paid_submi))


#%%
for e in paid_engage:
    if e['num_courses_visited'] > 0:
        e['has_visited'] = 1
    else:
        e['has_visited'] = 0

#%%
paid_eng_in_week = []
for e in paid_engage:
    acc = e['account_key']
    join_dt = paid_students[acc]
    engage_dt = e['utc_date']
    
    if oneweek(join_dt , engage_dt):
        paid_eng_in_week.append(e)
        
len(paid_eng_in_week)

#%%Group acc to account key
from collections import defaultdict
def group_by_key(data,key):
    grouped = defaultdict(list)
    for e in data:
        acc = e['account_key']
        grouped[acc].append(e)
    return grouped

#sum up for each acc     
def sumup_by_key(data, field_name):
    sum_by_key = {}
    for key , point in data.items():
        sumup = 0
        for e in point:
            sumup += e[field_name]
        sum_by_key[key] = sumup
    return sum_by_key
 
#total
import numpy as np
def total(data):
    print ('Mean:',np.mean(data))
    print ('Std:',np.std(data))
    print ('Min:',np.min(data))
    print ('Max:',np.max(data))

#%%avg minutes

eng_by_acc = group_by_key(paid_eng_in_week , 'account_key')
tmin_by_acc = sumup_by_key(eng_by_acc , 'total_minutes_visited')
total_minutes = list(tmin_by_acc.values())
total(total_minutes)
#lessons completed

eng_by_acc = group_by_key(paid_eng_in_week , 'account_key')
tless_by_acc = sumup_by_key(eng_by_acc , 'lessons_completed')
total_lessons = list(tless_by_acc.values())
total(total_lessons)

#courses completed

eng_by_acc = group_by_key(paid_eng_in_week , 'account_key')
tcourse_by_acc = sumup_by_key(eng_by_acc , 'has_visited')
total_courses = list(tcourse_by_acc.values())
total(total_courses)
#%%Max minutes spending Student

maxmin_stu = None
max_min = 0
for student , total_min in tmin_by_acc.items():
    if total_min > max_min:
        max_min = total_min
        maxmin_stu = student
print (max_min)


for e in paid_eng_in_week:
    if e['account_key'] == maxmin_stu:
        print (e)
        
#%%SUBMISS
project_keys = ['746169184','3176718735']
pass_proj = set()
for s in paid_submi:
    key = s['account_key']
    project = s['lesson_key']
    rating = s['assigned_rating']
    if project in project_keys and (rating == 'PASSED' or rating == 'DISTINCTION'):
        pass_proj.add(key)
        
len(pass_proj)

passing_engagement = []
non_passing_engagement = []
for e in paid_eng_in_week:
    if e['account_key'] in pass_proj:
        passing_engagement.append(e)
    else:
        non_passing_engagement.append(e)
        
print (len(passing_engagement))
print (len(non_passing_engagement))
