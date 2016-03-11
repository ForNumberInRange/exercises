__author__ = 'dozie9'

import datetime

today = datetime.date.today()
name = raw_input('Pls. Enter your name: ')
age = raw_input('Pls. Enter your age: ')
age_dif = 100 - eval(age)
i00Years = age_dif + today.year

print 'Hi! %s. You wold be 100years in year %d' %(name,i00Years)