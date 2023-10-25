import datetime
from random import randint


month = randint(7, 10)
if month == 10:
    day = randint(1, 25)
else:
    day = randint(1, 30)
date = datetime.date(2023, month, day)
date_now = date.today()
print(date)
print(date_now)
delta = datetime.timedelta(days=7)
print(date_now-date)
if date_now-date > delta:
    print('True')
else:
    print('False')
