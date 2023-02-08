# 11021
# testCase with Case#n

import sys

T = int(input())

for i in range(1, T+1):  # case 수가 1부터 입력되도록 하기 위함
    A, B = map(int, sys.stdin.readline().rstrip().split())  # 빠른 입력 받기
    print("Case #%s: %s" % (i, A+B))