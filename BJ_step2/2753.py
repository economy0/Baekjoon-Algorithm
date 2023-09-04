# 2753
# 윤년 : 4의 배수 & not 100의 배수 이거나 400의 배

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400):  # 같지 않다 : !=
    print("1")
else:
    print("0")
