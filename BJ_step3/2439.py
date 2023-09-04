# 2439
# 별찍기2

N = int(input())

for i in range(N):
    i += 1
    if N-i == 0:  # 마지막 줄에는 공백 없이 출력
        print("*" * i)
    else:
        print(" " * (N-i-1), "*" * i)  # 별 i 만큼 찍기


# 다른 풀이
N = int(input())

for i in range(1, N+1):
    print(" " * (N-i) + "*" * i)

# 차이점
# print 할 때, 콤마로 연결해서 쓰면 공백이 생김.
# 하지만 + 를 사용하면 공백없이 출력 가능.
# 나의 풀이에서 조건문이 들어간건 공백 때문인데, + 를 사용한다면 간략한 풀이 가능.
