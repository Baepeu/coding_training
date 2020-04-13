# 복리 계산 문제
# 입력 : 원금, 연이율, 투자기간, 지급횟수
# 출력 : 원리금

principal = input("What is the principal amount? ")
rate = input("What is the rate: ")
years = input("What is the number of years: ")
compounded_per_year = input("What is the number of times the interest\nis compounded per year: ")

# 형변환
principal = float(principal)
rate = float(rate)
years = int(years)
compounded_per_year = int(compounded_per_year)

final_amount = principal * (1 + rate/100/compounded_per_year)**(compounded_per_year*years)

msg = f"${principal} invested at {rate}% for {years} years compounded {compounded_per_year} times per year is ${final_amount:.2f}"

print(msg)