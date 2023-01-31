# 자료형
# None 값이 없는 값
None # 컴퓨터왈) 난몰라

print(None)
print(0 == None)    # None은 0이 아니다
print('' == None)   # None은 ''이 아니다

#숫자형
val = 3         # 정수 int
print(type(val))

val = 3.14      # 실수 float
print(type(val))

val = 'Hello'   # 문자 str
print(type(val))

val = 0b1010    # 이진수도 int형
print(type(val))

val = 4_520_000
print(val)

val = 3_099.99
print(val)

# 문자열
val = 'Lifeis short, "You need Python.'
print(val)
print(type(val))

val = 'Hell\nWorld!'    # \n : 줄바꾸기
print(val)
val = 'Hell\tWorld!'    # \t : tap키
print(val)
val = 'Hell\t\bWorld!'  # \b : 백스페이스키
print(val)

val = '''Life is short,
You need Python'''      # ''' ''' : 줄바꿔서 이어서 가능
print(val)
val = "Hi, I'm 'jeongjae'"  # "" 안에 '' 쓸때
print(val)
val = 'Hi, I\'m \'jeongjae\''   # '' 안에 '' 쓸때
print(val)

# 불린형 or 불형
참 = True   # 대문자해야함
거짓 = False
print(type(거짓))   # bool타입

print(1 + 1 == 2)
# 거짓이라는 False 값 변수가 참인가
print(거짓 == True)
print(거짓 == False)
print(거짓 is False)    # 거짓이 거짓이냐

print(bool(1))  # 1 == true
print(bool(0))  # 0 == False
print(bool(2))  # 0빼고 true가 나옴 하지만 1을 쓸것

