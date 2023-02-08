# 10950
# 테스트 케이스 입력 후, 각각의 결과 출력

T = int(input())

for i in range(T):  # T번 만큼 반복시행
    A, B = map(int, input().split())  # T번 만큼 입력받기
    print(A+B)  # 결과 출력
