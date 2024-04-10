# 베르트랑 공준 
"""
n < 적어도 하나의 소수 <= 2*n  (자연수이면서 소수)
-> 자연수 n이 주어질때 n보다 크고 2n보다 작거나 같은 소수의 개수 출력 

입력 : 1 < n <= 123456
"""
# ver 1
# import sys
# input = sys.stdin.readline

# #에라토스테네스의 채
# nums = [i for i in range(246912+1)]
# for i in range(2,len(nums)):
#     for j in range(2*i,len(nums),i):
#         if nums[j] != 0:
#             nums[j] = 0

# while True:
#     n = int(input())
#     if n == 0:
#         break

#     cnt = 0
#     for j in nums[n+1:2*n+1]:
#         if j != 0:
#             cnt += 1
#     print(cnt)



# ver 2
import sys
input = sys.stdin.readline

#에라토스테네스의 채
nums = [i for i in range(246912+1)]

for i in range(2, int(len(nums) ** 0.5) + 1):  # 최적화 부분 (200ms 차이)
    if nums[i]:
        for j in range(i*i, len(nums)+1, i):
            nums[j] = 0


while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for j in nums[n+1:2*n+1]:
        if j != 0:
            cnt += 1
    print(cnt)