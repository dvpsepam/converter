import os
import datetime# import datetime
import json
from urllib.request  import urlopen
import pandas as pd 

url_kursy = "http://api.nbp.pl/api/exchangerates/rates/a/usd/2022-01-01/2022-12-31/"

# specify the year for which you want to get the weekdays
year = 2022

# create a datetime object for the first day of the year
date = datetime.date(year, 1, 1)

def get_workdays_dates():
    # loop over all the days in the year
    while date.year == year:
        # check if the day is a weekday (Monday = 0, Sunday = 6)
        if date.weekday() < 5:
            # if it's a weekday, print the date
            print(date)
    
        # increment the date by one day
        date += datetime.timedelta(days=1)

# read 
def read_from_api():
        
    data_from_bank = urlopen(url_kursy)
    dict_kursy = json.loads(data_from_bank.read())

    for rate in dict_kursy["rates"]:
        print(datetime.datetime.strptime(rate["effectiveDate"], '%Y-%m-%d'))

