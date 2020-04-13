# 입력 : 구매금액, 주
# 출력 : 중간합계, 세금, 총 합계

amount = input("What is the order amount? ")
state = input("What is the state? ")

# 형변환
amount = float(amount)

tax = amount * 0.055
total = amount + tax

if state == 'WI':
    print(f"The subtotal is ${amount:.2f}")
    print(f"The tax is ${tax:.2f}")

print(f"The total is ${total:.2f}")