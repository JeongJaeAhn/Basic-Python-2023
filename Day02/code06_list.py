# 복합형


# 리스트 안쓰면
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10

print(a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10)
print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)

# 리스트 == 배열 (파이썬에서만)
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
sum = 0
for i in arr:
    sum += i

print(sum)

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello', 13, 'World', True]
print(arr1)
print(arr2)
print(arr3)
print(type(arr3))   # 리스트 타입

arr4 = []   # 빈 리스트
arr5 = list()   # 빈 리스트
print(arr4)
print(arr5)

arr6 = [1,2,3,4,[6,7,8,[9,10]]]     # list안에 list 가능
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]]
print(arr7)

# 튜플
tuple1 = (1,2,3,4)
print(tuple1)

arr5.append(4)        # 리스트는 수정 변경 추가 삭제 다 됨
print(arr5)

## tuple1.append(4)    # 튜플은 수정 변경 추가 삭제 다 안됨
print(type(tuple1))   # 튜플 타입


# 딕셔너리   //비순차적
## 가로스크롤 늘리기 x
spiderman = { 'name' : 'Peter Parker',
              'age'  : 18,
            'weapon' : 'Web Shooter',
          'deserter' : '탈영병'}

print(spiderman)
print(spiderman['weapon'])
print(spiderman['age'])     # [] 안에 ctrl + space bar 딕셔너리 선택가능
print(type(spiderman))      # 딕셔너리 타입

# 집합 : 중복x
set1 = set([1,2,3,4])
print(set1)

set1 = set("Hello World")
print(set1)

