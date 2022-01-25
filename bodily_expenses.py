"""
Men: BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) – (5.677 x age in years)
"""

import time
from decimal import Decimal

WEIGHT = 86 # kg
HEIGHT = 190 # cm
AGE = 27 # years
GROCERY_BILL_PER_WEEK = 122 # dollars

grocery_bill_per_second = Decimal(GROCERY_BILL_PER_WEEK/7/24/60/60)

bmr = Decimal(1.2 * 4.184 * (88.362 + (13.397 * WEIGHT) + (4.799 * HEIGHT) - (5.677 * AGE)))

kj_per_second = bmr / (24*60*60)

counter = 0
while True:
   time.sleep(1)
   counter += 1
   print(f" Food cost for body maintenance after: {time.strftime('%H:%M:%S', time.gmtime(counter))} ${kj_per_second*grocery_bill_per_second*counter:.6f}", end="\r")
