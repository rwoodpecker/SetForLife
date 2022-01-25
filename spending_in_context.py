"""
A tool to put spending today in context of its future value. 
Spending $60 a month on streaming services might end up costing you the median salary!
Would you rather be able to watch the latest episode of some stupid show or have half a year of your life returned to you?
"""

from decimal import Decimal, InvalidOperation
REGULAR_OPTIONS = ["Y", "y"]
ONE_OFF_OPTIONS = ["N", "n"]
annual_returns = 0.0872

while True:
    try:
        net_income = Decimal(input("My after-tax income is: $"))
        regular = input("Is this spend a regular spend, e.g. a subscription (Y/N)? ")
        if regular not in (REGULAR_OPTIONS + ONE_OFF_OPTIONS):
            raise ValueError
        spend = Decimal(input("How much money am I spending if I spend this much on something: $"))
        if regular in REGULAR_OPTIONS:
            times_per_year = Decimal(input("This many times per year: "))
            years = int(input("Over this many years: "))
        else:
            years = int(input("In this many years: "))
    except InvalidOperation or ValueError:
        continue
    break

future_spend = 0
if regular in REGULAR_OPTIONS:
    yearly_spend = spend * times_per_year
    for i in range(1, years + 1):
        future_spend = (future_spend + yearly_spend) * Decimal((1+annual_returns))
    print(f"${round(future_spend, 2)} in {i} years (${spend * times_per_year * i} without growth)")
    print(f"You could buy an extra {future_spend/net_income:.2f} years off work ({future_spend*229/net_income:.2f} working days) in {years} years if you just stop buying that!")

else:
    for i in range(1, years + 1):
        spend = Decimal(spend * Decimal(1.07))
    print(f"Total cost is ${spend:.2f}")
    print(f"You could buy an extra {spend/net_income:.2f} years off work ({spend*229/net_income:.2f} working days) in {years} years if you just stop buying that!")
