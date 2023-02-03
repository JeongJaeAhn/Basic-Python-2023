# random 모듈 사용
import random

#print(random.choice(range(1, 7)))      # 1~6까지 랜덤으로 출력
numbers = [i for i in range(1, 46)]     # 1~45 리스트
lottery = []

for i in range(6):
    lottery.append(random.choice(numbers))

lottery = sorted(lottery)
print(lottery)