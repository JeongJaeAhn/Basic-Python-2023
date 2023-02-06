# 콘솔출력 보충
# 이스케이프 캐릭터(탈출문자)
print('1.Hello. \r\nWorld')
print('2.Hello. \nWorld')        # 이걸 권장

print('3.Hello. \n\tWorld')      # t는 탭
print('4.Hello. \n\t\bWorld')    # b는 백스페이스

print('5.Hello. \n\'World\'')    # \'는 문자열내 홑따옴표
print('6.Hello. "World"')
print('7.Hello. \\World\\')      # \\는 \를 문자열에 표현
print('8.Hello\0')

# 문자열 포맷팅 - 옛날방식
# %로 포맷코드를 시작
me = '저'
name = '정재'
age = 30
print('%s는 %s입니다. %d입니다.'%(me, name, age))

print(f'{254.112233:.2f}')  # 최신식
print('%.2f' %(254.112233)) # 옛날방식