# 혈중 알코올 농도 계산기
# 입력 : 몸무게, 성별, 음주량(잔수), 한잔당 알코올량, 경과시간
# 출력 : BAC (0.08미만여부)

weight = input("Your weight: ")
gender = input("Your gender(M or F): ")
count = input("How many do you drink: ")
alco_volume = input("How many alcohol in a drink: ")
time = input("Time after: ")
weight = float(weight)
count = float(count)
alco_volume = float(alco_volume)
time = float(time)

total_alco = count * alco_volume
r = 0.73 if gender == 'M' else 0.6
BAC = (total_alco*5.14/weight*r) - (0.015*time)

msg = f"Your BAC is {BAC}"
print(msg)
if BAC < 0.08:
    print("It is legal for you to drive.")
else:
    print("It is not legal for you to drive.")
