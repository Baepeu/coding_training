name = input("What is your name? ")
format_string = "Hello, %s, nice to meet you!"
"""
%? : 문자열 혹은 숫자 같은 데이터를 껴넣을 공간을 예약합니다.
%s, %c, %f, %d
%10s : 10자리를 확보하고 내용을 껴넣습니다. (오른쪽 정렬 기준)
%-10s : 왼쪽 정렬을 기준으로 합니다.
%0.2f : 소숫점 자릿수를 고정할 수 있습니다.
"""
msg = format_string % name # % 문법 혹은 format string
print(msg)