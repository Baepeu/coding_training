# 퇴직 계산기 - 현재 나이, 퇴직하고 싶은 나이
# 퇴직할 연도?
from datetime import datetime
# 현재 연도 구하기
current_year = datetime.now().year

# 나이 입력받기
current_age = input("What is your current age? ")
retire_age = input("At what age would you like to retire?")

# 형변환
current_age = int(current_age)
retire_age = int(retire_age)

# 계산
left_year = retire_age - current_age
retire_year = current_year + left_year

# 출력 문자열 만들기
msg = f"You have {left_year} years left until you can retire.\nIt's {current_year}, so you can retire in {retire_year}."

# 출력
print(msg)
