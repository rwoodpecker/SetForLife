"""
Calculates salary earned per second of work. Enter your annual post-tax salary below.
"""

import time

annual_salary = 100000 # enter your annual post-tax salary here
salary_per_second = annual_salary/220/7.5/60/60
start_time = 0

while True:
   time.sleep(1)
   start_time += 1
   print(f" Earnings after: {time.strftime('%H:%M:%S', time.gmtime(start_time))} ${salary_per_second*start_time:.2f}", end="\r")
