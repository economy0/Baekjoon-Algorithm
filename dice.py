# 2480
# 주사위 3개를 던져 상금받기

a, b, c = map(int,input().split())

if a==b==c:
    print(10000+(a*1000))
elif a==b!=c or a==c!=b:  # 두 경우 중 하나: or
    print(1000+(a*100))
elif b==c!=a:
    print(1000+(b*100))
else:  # 세가지 수 모두 다를 경우
    print(max(a,b,c)*100)