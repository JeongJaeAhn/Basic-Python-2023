# 라이프 스코프

# 전역변수
a = 1

## 지역변수
def vartest(x):
    global a # 전역에 있는 a를 함수(지역)에서 가져다 쓰겠다
    a = a + x + 1
    return a
##
a = vartest(a)
print(a)
#