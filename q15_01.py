# 암호검증
# 입력값 : 암호
# 출력값 : 올바른지 여부

password = "abc$123"
input_password = input("What is the password: ")

if input_password == password:
    print("Welcome!")
else:
    print("That password is incorrect.")