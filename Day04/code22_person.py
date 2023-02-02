# 클래스 생성
class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 생성자 추가
    # def __init__(self):
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'

    def __init__(self, name, height, gender) -> None: # None 안지워도됨
        self.name = name
        self.height = height
        self.gender = gender

    def walk(self):         # 무조건 self 입력
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다.')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

    # 2. 생성자외 매직메소드(펑션) __str__
    def __str__(self) -> str:
         return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'
    

jeongjae = Person('정재', 169, 'male') # 객체생성 instance
#jeongjae.name = '정재'
#jeongjae.height = '169'
#jeongjae.gender = 'male'
#jeongjae.blood_type = 'A'

print(f'{jeongjae.name}의 혈액형은 {jeongjae.blood_type}입니다.')

jeongjae.run('Fast')
print(jeongjae)

# 1. 초기화 후 객체생성
hong = Person('홍길동', 170, 'male')
hong.run('Slow')
print(hong)

print('======================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 165, 'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)