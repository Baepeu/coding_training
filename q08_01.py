# 피자 파티
# 입력값 : 몇명, 몇판, 한판당 조각수
# 출력 : 한사람 당 몇조각씩 먹고 몇조각이 남느냐?
# 연산자 : //(몫), %(나머지)
# 데이터 입력
people = input("How many people? ")
pizzas = input("How many pizzas do you have? ")
print()
pieces = input("How many pieces are in a pizza? ")

# 형변환
people = int(people)
pizzas = int(pizzas)
pieces = int(pieces)

# 계산
total_pieces = pizzas * pieces
per_pieces = total_pieces // people
leftover = total_pieces % people

# 출력 구문 만들기
msg = f"{people} people with {pizzas} pizzas\n"
msg += f"Each person gets {per_pieces} pieces of pizza.\n"
msg += f"There are {leftover} leftover pieces."

# 최종 결과 출력
print(msg)