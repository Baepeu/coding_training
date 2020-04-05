# 숫자 두개를 입력받고
# 사칙 연산 결과를 출력하시오.
# 제약조건 : 문자로 입력받는다.
first_number = input("What is the first number? ")
second_number = input("What is the second number? ")
# 형변환 : 새로저장할변수 = 바꾸고싶은타입(변수명)
first_number = int(first_number)
second_number = int(second_number)
print(first_number, "+", second_number, "=", first_number+second_number)
print(first_number, "-", second_number, "=", first_number-second_number)
print(first_number, "*", second_number, "=", first_number*second_number)
print(first_number, "/", second_number, "=", first_number/second_number)