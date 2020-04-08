# 셀프계산대 : 총 3개의 제품 가격과 갯수를 입력받는다.
# 가격 소계, 세금, 합계 금액

price1 = input("Price of item 1: ")
quantity1 = input("Quantity of item 1: ")
price2 = input("Price of item 2: ")
quantity2 = input("Quantity of item 2: ")
price3 = input("Price of item 3: ")
quantity3 = input("Quantity of item 3: ")

# 형변환
price1 = float(price1)
price2 = float(price2)
price3 = float(price3)

quantity1 = float(quantity1)
quantity2 = float(quantity2)
quantity3 = float(quantity3)

sub_total = price1 * quantity1 + price2 * quantity2 + price3 * quantity3

tax = sub_total * 0.055

total = sub_total + tax

msg = f"Subtotal: ${sub_total:.2f}\n"
msg += f"Tax: ${tax:.2f}\n"
msg += f"Total: ${total:.2f}"

print(msg)