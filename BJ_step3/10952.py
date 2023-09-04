# 10952
# 입력의 마지막에 0 0 입력

import sys

while True:  # 무한루프 발생
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a==0 & b==0:  # 0 0 입력 시, 무한루프 탈출
        break
    print(a+b)



