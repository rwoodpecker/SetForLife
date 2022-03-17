"""
Calculate how many minutes through the day you are
"""

from datetime import datetime, date, timedelta
import time

# Constants
SECONDS_IN_WORK_DAY = 8 * 60 * 60

# Get the time at 8am today
today = date.today()
work_start_date_time = datetime.combine(today, datetime.min.time()) + timedelta(hours=8)
work_endtime = work_start_date_time + timedelta(seconds=SECONDS_IN_WORK_DAY)


start_time = 0
while True:
    time.sleep(1)
    print(
        f"{((datetime.now() - work_start_date_time).seconds) * 100 / SECONDS_IN_WORK_DAY:.3f}% through the day",
        end="\r",
    )
