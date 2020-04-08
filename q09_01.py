from math import ceil
# round : 반올림, ceil : 올림, floor : 버림
# 입력 : 천장의 길이와 폭
# 출력 : 몇 리터가 필요한가?

# 입력
width = input("Width : ")
height = input("Height : ")
# 형변환
width = float(width)
height = float(height)

square_meters = width * height

# 올림
liters = ceil(square_meters / 9)

msg = f"You will need to purchase {liters} liters of paint to cover {square_meters} square meters"

print(msg)