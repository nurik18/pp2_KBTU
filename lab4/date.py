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

# работа с датами в питоне