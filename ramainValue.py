# 10430
# 나머지 값 구하기

A, B, C = map(int, input().split())  # 3개 이상의 정수형 변수 입력받기
print((A+B) % C)
print(((A%C) + (B%C)) % C)
print((A*B) % C)
print(((A%C) * (B%C)) % C)