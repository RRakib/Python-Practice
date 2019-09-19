############### Imports
import time
import calendar

############### Time
# print(time.time())
# print(time.ctime())
# print(time.localtime())
# print("Time altzone: ", time.altzone)
# print(time.asctime(time.localtime()))
# print(time.localtime()[2], "/", time.localtime()[1], "/", time.localtime()[0])

############### Calender
# print("Calendar: ", calendar.month(2019, 6))
# print(calendar.isleap(2019))

############### Date and Time
import time
from datetime import *
# epoctime = time.time()
# print(time.ctime(epoctime))
# today = datetime.datetime.today()
# print(datetime.datetime.today())
# print('{}/{}/{}'.format(today.day,today.month,today.year))
ldates = []
ldates.append(date(2019,2,5))
ldates.append(date(2016,9,5))
ldates.append(date(2019,1,5))
ldates.sort()
for date in ldates:
    print(date)