# 숫자 세개 입력받기
# 1. 같은 숫자가 있는 비교, 있다면 프로그램 종료
# 2. 제일 큰 수를 찾아서 출력하기.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

if (num1 == num2) or (num2 == num3) or (num3 == num1):
    print("There are same numbers.")
    exit()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3

print(f"The largest number is {max_num}.")


