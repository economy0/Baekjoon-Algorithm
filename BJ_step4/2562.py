# 2562
# 최댓값
# 9개의 서로 다른 자연수가 주어질 때,
# 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.


nums = [int(input()) for i in range(9)]  # 9번 동안 enter를 기준으로 수 입력받기
maxN = max(nums)  # 리스트의 최댓값

print(maxN)
print(nums.index(maxN) + 1)  # 인덱스 번호 + 1 출력



