# Test how well copilot can predict the next move

# Calculate compound interest on a principle amount over a number of years, at a given interest rate, adding a fixed amount to the principle at the end of each year
principle = 200000
years = 20
interest_rate = 0.06
fixed_amount = 4000 * 12
retire_years = 20
start = principle
for year in range(1, retire_years + 1):
    principle = principle * (1 + interest_rate) + fixed_amount
    print(f"Year {year}: ${principle:.2f} (contributions ${fixed_amount * year + start}, interest = {(principle - (fixed_amount * year + start)):.2f}")

for year in range(retire_years + 1, years + 1):
    principle = principle * (1 + interest_rate)
    print(f"Year {year}: ${principle:.2f} (contributions ${fixed_amount * retire_years + start}, interest = {(principle - (fixed_amount * year + start)):.2f} (increase of {principle * interest_rate}))")