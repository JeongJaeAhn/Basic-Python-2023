# 다중입력
# x, y = input('두 영단어를 입력하세요. > ').split()  # 공백으로 잘라서 따로

# print(x)
# print(y)

# 완전 다중입력(개수가 몇개든 상관없음)
# 중요!
inputs = list(map(str, input('단어를 입력하세요(개수상관x) > ').split()))   # map만쓰면 안됨 리스트화해야함

print(inputs)

inputs = list(map(int, input('정수를 입력하세요 > ').split()))

print(inputs)