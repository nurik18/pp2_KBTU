import datetime
today = datetime.date.today()
fiveDaysAgo = today - datetime.timedelta(days = 5)
print(fiveDaysAgo)
print()

# \\

print(f'Вчера: {today-datetime.timedelta(days=1)}')
print(f'Сегодня: {today}')
print(f'Завтро: {today+datetime.timedelta(days = 1)}')
print()

# \\

now = datetime.datetime.now()
print(now)
now = now.replace(microsecond=0)
print(now)
print()

# \\

from datetime import datetime

def difference_in_seconds(date1, date2):
    format_string = "%Y-%m-%d %H:%M:%S"
    dt1 = datetime.strptime(date1, format_string)
    dt2 = datetime.strptime(date2, format_string)
    return abs(int((dt2 - dt1).total_seconds()))

date1 = "2024-02-13 12:00:00"
date2 = "2024-02-14 12:00:00"

print(difference_in_seconds(date1, date2))
