name = input("What is your name? ")
format_string = "Hello, {}, nice to meet you!"
"""
{} : 왼쪽 정렬(<), 가운데(^), 오른쪽(>)
{:a^10s} : 10자리를 확보하고 문자열을 채우는데, 빈 공간은 a라는 문자로 채운다.
{:,.2f}
"""
msg = format_string.format(name) # .format 명령
print(msg)