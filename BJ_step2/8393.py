# 8393
# n 입력 후, 1부터 n까지의 합

n = int(input())
j = 0  # n까지의 수 합을 저장함

for i in range(n):
    i += 1
    j += i
print(j)
