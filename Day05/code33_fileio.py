# 파일 만들기
file = open('./Day05/../Day04/sample01.txt', 'w', encoding='utf-8')  # 상대경로
file = open('C:\DEV\Temp\Bank\sample01.txt', 'w', encoding='utf-8')  # 파일 쓰기로 만듦 / 절대경로(경로를 다적어주는것)

file.write('안녕하세요\n')
file.write('두번째 파일\n')
file.write('절대경로에 파일이 생성\n')

file.close()
print('sample01.txt가 생성되었습니다.')

# ASCII -> 한단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라언어를 다 표현가능

# 파일/폴더 경로
