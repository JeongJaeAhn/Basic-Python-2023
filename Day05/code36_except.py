# 예외처리
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

try:
    x, y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()
finally:
    print('계속되나요?')    # 이거 실행뒤 종료

# 원시적인 예외처리
# if y == 0:
#     print('y에 0을 넣지마세요')
#     exit()

print('계산 테스트')
try:
    print(div(x,y))
# except ZeroDivisionError as e:    # 굳이 쓸필요는없음
#     print('0으로 나누면 에러')
except Exception as e:              # 순서가 있음 Exception 은 제일마지막에 있어야함
    print(e)
finally:
    print('계산은 계속됩니다')

print(add(x,y))
print(mul(x,y))