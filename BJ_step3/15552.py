# 15552
# 빠른 테스트 케이스 만큼의 식 출력

import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())  # 시간초과 방지, rstrip() : 오른쪽 공백 삭제
    print(A+B)
