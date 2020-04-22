# 구매금액, 주, 위스콘신 주(카운티를 추가 입력)

order_amount = input("What is the order amount? ")
state = input("What state do you live in? ")

order_amount = float(order_amount)

state_tax = order_amount * 0.055
county_tax = 0
if state == "Wisconsin":
    county = input("What county do you live in? ")
    if county == "Eau Claire":
        county_tax = 0.05
    elif county == "Dunn":
        county_tax = 0.04
total_tax = state_tax + county_tax
msg = ""
if state in ["Wisconsin","Illinois"]:
    msg += f"The state tax is ${state_tax}\n"
    msg += f"The county tax is ${county_tax}\n"
    msg += f"The total tax is ${total_tax}\n"

total = order_amount + total_tax
msg += f"The total is ${total}"

print(msg)