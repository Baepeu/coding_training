from math import ceil

euros = input("How many Euros are you exchanging? ")
rate = input("What is the exchange rate? ")

euros = float(euros)
rate = float(rate)

dollars = ceil(euros * rate / 100 * 100) / 100

msg = f"{euros} Euros at an exchange rate of {rate} is {dollars} dollars"

print(msg)