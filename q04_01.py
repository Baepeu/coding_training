# 문자열 보간
# % 문법
# str.format() 메서드
# python 3.6 부터 등장한 f string
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
msg = f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"
print(msg)