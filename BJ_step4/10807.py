# 10807
# 개수 세기

N = int(input()) # data 정수의 개수
data = list(map(int, input().split()))
v = int(input()) # 찾으려는 정수

if v in data:
  print(data.count(v))
else:
  print("0")
