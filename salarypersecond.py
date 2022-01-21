import time

annualSalary = 100000 # enter your annual post-tax salary here
salaryPerSecond = annualSalary/220/7.5/60/60

stime = 0

while True:
   time.sleep(1)
   stime += 1
   print(f" Earnings after: {time.strftime('%H:%M:%S', time.gmtime(stime))} ${salaryPerSecond*stime:.2f}", end="\r")
