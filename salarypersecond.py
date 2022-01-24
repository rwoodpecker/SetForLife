"""
Calculates salary earnt per second of work. Enter your annual post-tax below.
"""

import time

# enter your annual post-tax salary here
annual_salary = 100000 
salary_per_second = annual_salary/220/7.5/60/60
start_time = 0

while True:
   time.sleep(1)
   start_time += 1
   print(f" Earnings after: {time.strftime('%H:%M:%S', time.gmtime(start_time))} ${salary_per_second*start_time:.2f}", end="\r")
