"""
What is the input string? Homer
Homer has 5 characters.
"""
# 문자열의 길이를 어떻게 알 수 있을까?
# 내장함수? len()
"""
msg = "Homer"
msg_length = len(msg)
print(msg_length)
"""

msg = input("What is the input string? ")
msg_length = len(msg)
format_string = "%s has %d characters."
print_string = format_string % (msg, msg_length)
print(print_string)
