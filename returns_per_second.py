"""
Calculate expected earnings per second on your portfolio
"""

import time
from decimal import Decimal

PORTFOLIO_SIZE = 180000
REAL_ANNUAL_RETURN = Decimal(8.72/100)

yearly_return = PORTFOLIO_SIZE * REAL_ANNUAL_RETURN
earnings_per_second = Decimal(yearly_return / (365*24*60*60))
seconds = 0
while True:
   time.sleep(1)
   seconds += 1
   print(f" Earnings after: {time.strftime('%H:%M:%S', time.gmtime(seconds))} ${earnings_per_second*seconds:.4f}", end="\r")