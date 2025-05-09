from datetime import datetime, timedelta

now = datetime.now()
# print(now - timedelta(1))

year = now.strftime("%Y/%m/%b, %H:%M%p")
print(year)