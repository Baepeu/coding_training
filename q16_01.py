# 합법적 운전 가능한 연령?
# 입력 : 나이
# 출력 : 운전 가능 여부

age = input("What is your age? ")
age = int(age)

if age >= 16:
    print("You are old enough to legally drive.")
else:
    print("You are not old enough to legally drive.")