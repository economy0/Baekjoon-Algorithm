# 2884
# 알람시계

H, M = map(int, input().split())

if H > 0 and M < 45:
    print(H - 1, 60 - (45 - M))
elif H == 0 and M < 45:  # H가 0일때 H-1이면 H = -1이 되므로, 조건 하나를 추가함
    print("23", 60 - (45 - M))
else:  # M > 45
    print(H, M - 45)