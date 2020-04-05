# 문자열 안에 따옴표 출력하기
# 1. escape 문자 사용하기
# 2. 문자열 보간(양식 문자열)
# 3. 문자열 대체(replace)

# 1. 문장 입력받기
sentence = input("What is the quote?")
# 2. 발언자 입력받기
speaker = input("Who said it?")
# 3. 문장으로 만들어 출력하기
msg = speaker + " says, \"" + sentence + "\""
print(msg)

"""
escaping -> \n,\t, \b, \", \'
"""