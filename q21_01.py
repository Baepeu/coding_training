# 월 숫자 입력
# 월 영문 출력

months = {
    "1":"January","2":"February","3":"March",
    "4":"April","5":"May","6":"June","7":"July",
    "8":"August","9":"September","10":"October",
    "11":"November","12":"December"
}

month = input("Please enter the number of the month: ")

if month in months:
    msg = f"The name of the month is {months[month]}"
    print(msg)
else:
    print("There is no month.")