# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:25:18 2021

@author: hp
"""

# i defined my own floor function since im not allowed to import
def floor(no):
    stringed_no = str(no)
    
    if '.' in stringed_no:
        number = stringed_no.partition('.')
        integer_number = int(number[0])
    else:
        integer_number = no
        
    return integer_number

def add_time(start, duration, current_day = None):
    if current_day:
        day = current_day.lower()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    current_time = start.partition(':')
    added_time = duration.partition(':')
    am_or_pm = current_time[2][-2:]
    y = list(current_time[0:2])
    y.append(str(current_time[2]).rstrip(' PMA'))
    new_current_time = tuple(y)
    hours = int(new_current_time[0])+ int(added_time[0])
    minutes = int(new_current_time[2]) + int(added_time[2])
    
    if minutes > 60:
        adjusted_minute = minutes%60
        add_min_to_hour = floor(minutes/60)
        if adjusted_minute < 10:
            adjusted_minute = '0' + str(adjusted_minute)
        else:
            adjusted_minute = str(adjusted_minute)
    
    else: 
        adjusted_minute = minutes
        if adjusted_minute < 10:
            adjusted_minute = '0' + str(adjusted_minute)
        else:
            adjusted_minute = str(adjusted_minute)

    
    if hours > 12:
         adjusted_hour = hours%12
       # adjusted_hour24 = hours % 24
    else:
         adjusted_hour = hours
        #adjusted_hour24 = hour24
    
    adjusted_hour += 1
    
    if am_or_pm == 'AM':
        hour24 =  hours
    else:
        hour24 = hours + 12
        
    total_days_added = (hour24 + add_min_to_hour  ) / 24
    print(hour24)
    print(total_days_added)
    
    days_later = total_days_added
    
    
    if floor(total_days_added) == 0:
            days_later = 0
    else:
        if days_later - floor(days_later) != 0:
            print(days_later)
            days_later = floor(days_later) + 1
            print(days_later)
        else:
            days_later = floor(days_later)
            
    new_index_control = days.index(day) + days_later
            
    
    if new_index_control < 7:
            new_day_index = new_index_control
            
    else:
            new_day_index = new_index_control%7

    
    x = round(new_day_index)
    new_day = days[x]
    #day_adjuster_lenght = len[n for n in range(0, hours+1, 24)]
    
    
    am_pm_adjuster = [round(no/12) for no in range(0, (hours+1), 12)]
    
    if am_or_pm == 'PM':
        am_pm_adjusted = ['PM' if no%2 == 0 else 'AM' for no in am_pm_adjuster]
    else:
        am_pm_adjusted = ['AM' if no%2 == 0 else 'PM' for no in am_pm_adjuster]
    
    if current_day:
        new_time = '{} : {} {} {} ({} days later)'.format(str(adjusted_hour), adjusted_minute, am_pm_adjusted[-1], new_day, days_later)
    elif current_day and days_later == 1:
        new_time = '{} : {} {} {} (next day)'.format(str(adjusted_hour), adjusted_minute, am_pm_adjusted[-1], new_day)
    elif days_later == 1:
        new_time = '{} : {} {} (next day)'.format(str(adjusted_hour), adjusted_minute, am_pm_adjusted[-1])
    else:
        new_time = '{} : {} {} ({} days later)'.format(str(adjusted_hour), adjusted_minute, am_pm_adjusted[-1], days_later)
    """ error checking prints here
    print(new_time)
    print(days_later, 'days later')
    print(new_day_index)
    print(days.index(day))
    print(new_day) """
    return new_time

'''
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
 
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
 
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later) '''

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
 
