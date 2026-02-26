#dates subtract five days from current date.
from datetime import datetime, timedelta
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print(five_days_ago)


#print yesterday, today, tomorrow.
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print(yesterday)
print(current_date)
print(tomorrow)
#output: 2026-02-25 12:34:56
#output: 2026-02-26 12:34:56
#output: 2026-02-27 12:34:56


#drop microseconds from datetime.
current_date_without_microseconds = current_date.replace(microsecond=0)
print(current_date_without_microseconds)
#output: 2024-06-01 12:34:56



#calculate two date difference in seconds.
date1 = datetime(2024, 6, 1)
date2 = datetime(2024, 6, 10)
date_difference = date2 - date1
difference_in_seconds = date_difference.total_seconds()
print(difference_in_seconds)
#output: 777600.0