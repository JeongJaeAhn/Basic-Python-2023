# studyPython2023
부경대 IoT 파이썬 학습 리포지토리

## 1일차
1. 기본구성
    - Git/Github 설치 및 연동
    - Visual Studio code 설치 및 연동
    - Python 설치
2. 파이썬 기본
    - 콘솔출력
    - 주석

```python
# desc : 콘솔출력 - 주석
print('Hello, Python!!') # 콘솔출력 함수
```

## 2일차
1. 파이썬 기본
    - 변수
    - 자료형
    - 연산자

```python
# 변수
val = 1                             # val에 값 1을 대입

# 자료형
print(type(val))                    # <class 'int'> val의 자료형은 정수형

# 문자열 포맷팅
pi = 3.141592
print(f'파이는 {pi}입니다.')        # pi는 3.141592 입니다.
print(f'파이는 {pi:0.2f}입니다.')   # pi는 3.14 입니다.
print(f'파이는 {pi:10.3f}입니다.')  # pi는         3.142 입니다.
```

## 3일차
1. 파이썬 기본
    - 흐름제어
        - if
        - for
        - while
    - 구구단 프로그램
    - 함수

## 4일차
1. 파이썬 기본
    - 가상환경
    - 객체지향 OOP
    - 패키지, 모듈

## 5일차
1. 파이썬 기본
    - 패키지 계속
    - 입출력 다시
    - 예외처리

## 6일차
1. 파이썬 기본
    - 콘솔출력 보충
    - 객체지향 다시
        - 객체지향 특징
        - 상속, 다중 상속

2. 파이썬 응용
    - 주소록 프로그램 [소스](https://github.com/JeongJaeAhn/studyPython2023/blob/main/Project/address_app.py)

![실행화면](https://raw.githubusercontent.com/JeongJaeAhn/studyPython2023/main/images/address_app.png)
실행화면

## 7일차
1. 파이썬 응용
    - 주피터 노트북 사용법
        - 노트북 생성 : 파일메뉴 - 새파일
    - 리스트 연산 추가
    - 라이브러리 사용법
        - folium (지도 라이브러리)

## 8일차
1. 파이썬 응용
    - 라이브러리 사용법
        - urllib.request
    - 웹 크롤링([소스]https://github.com/JeongJaeAhn/studyPython2023/blob/main/Day08/code44_web_crawling_tutorial.ipynb)
        - 기상청 오늘의 날씨 크롤링
        - 데이터포털 OpenAPI 크롤링
        - BeautifulSoup 크롤링

![실행화면](https://raw.githubusercontent.com/JeongJaeAhn/studyPython2023/main/images/jupyter_folium.png)

folium openAPI 연동화면

## 9일차
1. 파이썬 응용
    - GUI 개발
        - Tkinter 소개
        - PyQt 소개, 설치
        - PyQt 기본 사용법
        - 위젯

## 10일차
1. 파이썬 응용
    - GUI 개발
        - PyQt 위젯 계속
        - PyQt 다이얼로그

![실행화면](https://raw.githubusercontent.com/JeongJaeAhn/studyPython2023/main/images/dialog.png)

PyQt 실행화면