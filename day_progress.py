"""
Calculate what % through the work day you are
"""

from datetime import datetime, date, timedelta
import time
import platform
import os

# Constants
# Change this if your work day is longer or shorter than 8 hours
WORK_START_HOUR = 8
HOURS_IN_WORK_DAY = 8
SECONDS_IN_WORK_DAY = HOURS_IN_WORK_DAY * 60 * 60

# Get work start time and end time
today = date.today()
work_start_date_time = datetime.combine(today, datetime.min.time()) + timedelta(
    hours=WORK_START_HOUR
)
work_endtime = work_start_date_time + timedelta(seconds=SECONDS_IN_WORK_DAY)

# Print how far through the day you are in %.
while True:
    time.sleep(1)
    progress = (
        ((datetime.now() - work_start_date_time).seconds) * 100 / SECONDS_IN_WORK_DAY
    )
    print(
        f"{progress:.3f} % through the day...",
        end="\r",
    )
    if progress >= 100:
        # Show a notification (macOS)
        if platform.system() == "Darwin":
            os.system(
                'osascript -e \'display notification "Work day over" with title "Work day over"\''
            )
        sys.exit()
