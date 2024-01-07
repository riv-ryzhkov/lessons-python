# pip install python-dateutil
import sys
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *

# print(sys.path)
# sys.path.insert(0, 'D:\\')
# print(sys.path)

# now = parse("Sat Nov 13 17:13:46 UTC 2021")
# print(now)
# today = now.date()
# time = now.time()
# print(today)
# print(time)
# month, day, weekday = map(int, (input('month day weekday: ').split()))
# year = rrule(YEARLY, dtstart=now, bymonth=month, bymonthday=day, byweekday=weekday)[0].year
# rdelta = relativedelta(easter(year), today)
# print("Today is: %s" % today)
# # Today is: 2003-10-11
# print("Year with next Nov 11th on a Friday is: %s" % year)
# # Year with next Aug 13th on a Friday is: 2004
# print("How far is the Easter of that year: %s" % rdelta)
# # How far is the Easter of that year: relativedelta(months=+6)
# print("And the Easter of that year is: %s" % (today+rdelta))
# # And the Easter of that year is: 2004-04-11