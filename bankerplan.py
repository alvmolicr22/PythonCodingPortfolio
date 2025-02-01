# solution to Banker's plan - test what happens
# https://www.codewars.com/kata/56445c4755d0e45b8c00010a

def fortune(f0, p, c0, n, i):
    # Convert percentages to decimal values
    interest_perc = p / 100
    inflation_perc = i / 100

    # list for yearly balance
    end_of_year_balance = []

    # Iterate through each year
    for year in range(1, n):
        # Calculate the interest earned
        f0 += int(f0 * interest_perc)

        # Deduct the withdrawal amount
        f0 -= c0

        # Append the balance to the list
        end_of_year_balance.append(f0)

        # Check if the balance becomes negative
        if f0 < 0:
            return False, end_of_year_balance

        # Adjust the withdrawal amount for inflation
        c0 = int(c0 * (1 + inflation_perc))

    return True, end_of_year_balance


initial_deposit_input = float(input("Type the amount of the initial deposit: "))
annual_rate_input = float(input("Type the amount of the annual interest rate: "))
annual_withdraw_input = float(input("Type the annual withdrawal amount: "))
years_input = int(input("Type the total of years of the plan :"))
inflation_rate_input = float(input("Type the annual inflation rate: "))

print(fortune(initial_deposit_input, annual_rate_input, annual_withdraw_input,
              years_input, inflation_rate_input))
