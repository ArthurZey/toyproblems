#!/usr/bin/env python

'''
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import datetime

start_date = datetime.datetime.strptime('1901-01-01', '%Y-%m-%d').date()
end_date   = datetime.datetime.strptime('2000-12-31', '%Y-%m-%d').date()

date = start_date
num_sundays_on_first_of_month = 0
while date != end_date:
  if date.weekday() == 6 and date.day == 1:
    num_sundays_on_first_of_month += 1
  date += datetime.timedelta(days=1)

print(num_sundays_on_first_of_month)