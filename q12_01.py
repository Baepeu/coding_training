from math import ceil

# A = P(1+rt)

principal = input("Enter the principal: ")
interest = input("Enter the rate of interest: ")
years = input("Enter the number of years: ")

# 형변환
principal = float(principal)
interest = float(interest)
years = int(years)

total = ceil(principal * (1 + interest/100*years)*100)/100
msg = f"After {years} at {interest}%, the investment will be worth ${total}"

print(msg)