# 연산자
# 할당연산 assignment
# 2 = 1 (x)
val = 1

# equal 연산자
print(1 == 1)

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(1024 / 2)     # 나누기 실수형으로
print(1024 // 2)    # 나누기 정수형으로
print(6 // 3)       
print(6 % 3)        #나머지    배수를 찾을때 씀

#print(6 / 0)       # 0 나누기는x 무한대 에러뜸
#print(6 // 0)

print(2 ** 10)      # 2의 10승

# 문자열연산
first = 'Hello'
second = 'World'
print(first + second)   # 문자열에선 + , * 만 가능
print(first + ' ' + second) # 문자열 연산할때 공백넣기
print(first, second)

print(first * 4)

print(len(first))   # len() : 문자열 길이
print(first[0])     # [] : 리스트
print(first[1])
print(first[2])
print(first[3])
print(first[4])
#print(first[5])    # IndexError

# 파이썬에서 인덱스 찾는 특이한 방법
print(first[-1])    # 마지막것을 출력
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

# 리스트 자르기
current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[0:4]) # 0번째부터 4번째까지
print(current[5:7]) # 5번째뒤부터 7번째까지
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:]) # :공백은 마지막까지

print(current[-19:-15]) # 2023
print(current[-19:4]) # 2023

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7  # 0번째에 값 7을 넣어라

print(que)

que.append(10)      # 맨 마지막에 추가
print(que)

que.insert(3, 99)   # 특정인덱스에 추가 / 3번째에 99를 넣음
print(que)

que.remove(10)      # 해당 값 삭제 / 값10을 지움
print(que)

# 튜플은 안됨
# tup = (1, 2, 3, 4, 5)
# tup[1] = 9

# print(tup)


# 문자열 == 문자 리스트
title = 'python'
print(title[0])

# title[0] = 'P'    # 문자열에서는 값변경 x
print('P' + title[1:])  # 응용방법

# 일반적인 문자형 리스트
text = ['p', 'y', 't', 'h', 'o', 'n']
print(text)
text[0] = 'P'   # 가능
print(text)

# 문자열 포맷팅 : {}에 .format(값)
print("I'm so happy {0} you, {1}!!".format(2, 'Hey'))
# 최신식 문자열 포맷팅  // 예) 홈페이지 로그인했을때 "OOO님 안녕하세요"
preword = 2
sayHello = 'Hey'
print(f"I'm so happy {preword} you, {sayHello}!!")

pi = 3.141592
print(f'파이는 {pi}입니다.')
print(f'파이는 {pi:0.2f}입니다.')  # 0.2f : 소수점 두번째까지만 출력
print(f'파이는 {pi:10.3f}입니다.') # 10.3 : 앞 10번째 만큼(공백이생김), 소수점 반올림하여 세번째까지 출력

# 문자열을 특정문자로 자르기
full_name = 'Jeong Jae Ahn'
vals = full_name.split()    # 스페이스 자르기
print(type(vals))   # 리스트
print(vals)

vals = full_name.split('e') # e로 지정하여 자르기
print(vals)

print(full_name.replace('Ahn', 'An'))   # 바꾸기

# 문자열 공백 없애기
hi = '           Hello~ Bye~         '
print(hi.lstrip() + '|')    #왼쪽공백없애기
print(hi.rstrip() + '|')    #오른쪽공백없애기
print(hi.strip() + '|')     #양쪽공백없애기

# 문자열에서 값을 찾기
print(full_name.index('A'))     # 'A' 문자 및 단어의 시작 위치를 알려줌

print(full_name.find('Z'))      # Z가 없어서 -1로 나옴
print(full_name.find('A'))      # 인덱스와 값이 같음

# 찾는 단어의 개수
print(full_name.count('e'))     # e가 몇개 있는지

# 모든 단어를 대문자/소문자로 변경
print(full_name.upper())        # 전부 대문자
print(full_name.lower())        # 전부 소문자


# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)