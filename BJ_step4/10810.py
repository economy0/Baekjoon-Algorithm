# 10810
# 공 넣기

N, M = map(int, input().split())
ball = list(0 for i in range(N))  # 바구니 갯수만큼 길이의 리스트 생성

for i in range(M):  # M번 공을 넣기 위한 반복문
    i, j, k = map(int, input().split())  # 공 넣기
    ball[i-1:j] = [k]*(j-i+1)  # 값 삭제하고 k를 연속적으로 추가하기

print(*ball)  # *ball : 리스트 요소 한번에 출력



# a = [1,2,3]
# a[2:3]=[4]  # 2자리 값을 삭제하고 3자리 전에 데이터 삽입
# print(a)
# >> 1,2,4