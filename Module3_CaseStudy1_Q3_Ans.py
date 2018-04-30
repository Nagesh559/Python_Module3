# Weather forecasting organization wants to show is it day or night.
# So, write a program for such organization to find whether is it dark outside or not.

import datetime
from time import *
def check_if_ligh_or_dark(list_date_time):
    if int(list_date_time[0])<6 & int(list_date_time[1]<=59):
        return 'Day'
    if int(list_date_time[0])>6 & int(list_date_time[1]<=59):
        return 'Night'
    if int(list_date_time[0])<6:
        return 'Night'

currentDt = datetime.datetime.now()
list1=list()
list1.append(str(currentDt.hour))
list1.append(str(currentDt.minute))
print check_if_ligh_or_dark(list1)

