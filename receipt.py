# 25304
# 영수증 총 금액과 실제 구매한 금액의 일치 여부

X = int(input())  # 총 금액
N = int(input())  # 물건 개수
j = 0  # 실제 금액의 합 저장

for i in range(N):
    a, b = map(int, input().split())
    c = a*b
    j += c

if j==X:  # 총 금액과 실제 금액이 일치
    print("Yes")
else:  # 총 금액과 실제 금액이 불일치
    print("No")

