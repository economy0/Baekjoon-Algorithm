# 10951
# 여러개의 테스트케이스 출력
# try: 변수 A,B에 int 형이 들어간다면, A+B의 값을 출력한다.
# except: try 에 대한 에러가 발생한 경우 (ex. a 1, 3, 2 ㄱ 입력)

import sys

while True:  # 무한루프 발생
    try:
        A, B = map(int, sys.stdin.readline().rstrip().split())  # 빠른 입력 받기
        print(A+B)
    except:  # try 에 대한 에러가 발생한 경우 무한루프 탈출
        break