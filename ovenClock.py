# 2525
# 오븐 시계

A, B = map(int, input().split())  # 시, 분
C = int(input())  # 추가 분
n = (B+C) // 60  # 몫 (괄호 표기하여 계산 순서 주의하기)

if A+n >= 24:  # A <= 23 이므로 B+C가 무조건 60이상이라는 뜻
    print(A+n-24, (B+C)-(n*60))
else:  # A+n < 24
    if B+C < 60:
        print(A, B+C)
    else:  # 60분 이상
        print(A+n, (B+C)-(n*60))