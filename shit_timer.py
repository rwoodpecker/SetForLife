'''Tracks the amount of time spent and value of shitting'''

from pathlib import Path
import time

annual_salary = 100000 # enter your annual post-tax salary ($) here
salary_per_second = annual_salary/220/7.5/60/60
this_time = 0 
file_name = '.timer.txt'

Path(file_name).touch(exist_ok=True)

with open(file_name, 'r+') as file:
    if not file.read():
        total_time = 0
        file.write(str(total_time))
        file.close
    else:
        file.seek(0)
        total_time = int(file.read())
        file.close
try:
    while True:
        time.sleep(1)
        total_time += 1
        this_time += 1
        print(f" Earnings during this shit: {time.strftime('%H:%M:%S', time.gmtime(this_time))} ${salary_per_second*this_time:.2f}. Total shit earnings: {time.strftime('%H:%M:%S', time.gmtime(total_time))} ${salary_per_second*total_time:.2f}", end="\r")
except KeyboardInterrupt:
    pass
    with open(file_name, 'w') as file:
        file.write(str(total_time))
        file.close
