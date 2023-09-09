# 10871
# x보다 작은 수
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

N, X = map(int, input().split())  # N과 X 입력 받기
A = list(map(int, input().split()))  # 수열 A 리스트 형태로 입력 받기

for i in A:  # 리스트 A 내의 원소를 i로 취급
    if i < X:  # 원소 i가 X보다 작다면
        print(i, end=" ")  # i를 공백으로 구분해 출력
