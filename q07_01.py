# 가로, 세로 피트 단위로 숫자 입력받기
# 결과 1 : 제곱 피트 - 넓이
# 결과 2 : 제곱 미터 - 넓이

# 데이터 입력받기
length = input("What is the length of the room in feet? ")
width = input("What is the width of the room in feet? ")

# 형변환
length = float(length)
width = float(width)

# 계산
square_feet = length * width
square_meters = square_feet * 0.09290304

# 출력 구문 준비
msg = f"You entered dimensions of {length} feet by {width} feet\n"
msg += "The area is\n"
msg += f"{square_feet} square feet\n"
msg += f"{square_meters:0.3f} square meters"

print(msg)