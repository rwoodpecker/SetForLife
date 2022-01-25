"""
A tool to put spending today in context of its future value. 
Spending $60 a month on streaming services might end up costing you the median salary!
Would you rather be able to watch the latest episode of some stupid show or have half a year of your life returned to you?
"""

from decimal import Decimal, InvalidOperation

annual_returns = 0.0872

while True:
    try:
        spend = Decimal(input("How much money am I spending if I spend this much on something: "))
        times_per_year = Decimal(input("This many times per year: "))
        years = int(input("Over this many years: "))
    except InvalidOperation or ValueError:
        continue
    break

yearly_spend = spend * times_per_year
future_spend = 0

for i in range(1, years + 1):
    future_spend = (future_spend + yearly_spend) * Decimal((1+annual_returns))
    print(f"${spend} now is ${round(future_spend, 2)} in {i} years ({spend * times_per_year * i} without growth)")