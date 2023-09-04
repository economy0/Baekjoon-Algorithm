# 2588
# 계산과정을 보여주는 곱셈

A = int(input())
B = int(input())

p = int(B//100)  # 100의 자리수
q = int((B - p*100)//10)  # 10의 자리수
r = int(B - p*100 - q*10)  # 1의 자리수

print(A*r)
print(A*q)
print(A*p)
print(A*B)  # 최종 결과
