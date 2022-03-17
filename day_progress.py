"""
Calculate what % through the work day you are
"""

from datetime import datetime, date, timedelta
import time
import platform
import os
import sys


def day_progress():
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

    # Print how far through the day you are in %.
    while True:
        progress = (
            ((datetime.now() - work_start_date_time).seconds)
            * 100
            / SECONDS_IN_WORK_DAY
        )
        if progress >= 100:
            notify_and_exit()
        print(
            f"{progress:.3f} % through the day...",
            end="\r",
        )
        time.sleep(1)


def notify_and_exit():
    # Show a notification (macOS)
    if platform.system() == "Darwin":
        os.system(
            'osascript -e \'display notification "Work day over" with title "Work day over"\''
        )
    if platform.system == "Linux":
        os.system("notify-send 'Work day over'")
    print("\nWORK DAY OVER!!!\n")
    sys.exit()


if __name__ == "__main__":
    day_progress()
