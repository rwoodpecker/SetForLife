"""
A tool to help calculate approximately how much you get paid in real terms over 20 years when you win Set for Life.

Set for Life is a lottery with a jackpot that pays you out A$20,000 per month for 20 years.

Inflation is appled at the end of each year.
"""
from decimal import Decimal

# Put in your expected rate of inflation below
INFLATION_RATE = Decimal(2.5)

DEPRECIATION = 1 - (INFLATION_RATE/100)

INITIAL_PAYMENT = Decimal(20000)

YEARS = 20

MONTHS_PER_YEAR = 12

TOTAL_MONTHS_OF_PAYMENTS = MONTHS_PER_YEAR * YEARS

this_month_payment = INITIAL_PAYMENT
real_earnings = Decimal(0)
total_lost_to_inflation = Decimal(0)
for i in range(1, TOTAL_MONTHS_OF_PAYMENTS + 1):
    real_earnings += this_month_payment
    total_lost_to_inflation = total_lost_to_inflation + INITIAL_PAYMENT - this_month_payment
    print(f'Value at end of month {i}: ${round(real_earnings, 2)}. (Payment is ${round(this_month_payment, 2)}) Total lost to inflation: ${round(total_lost_to_inflation), 2}.')
    if i % 12 == 0:
        this_month_payment = this_month_payment * DEPRECIATION
print("Real earnings: ", round(real_earnings, 2), ". Total: ", round(real_earnings + total_lost_to_inflation, 2), ". Lost to inflation: ", round(total_lost_to_inflation, 2))
