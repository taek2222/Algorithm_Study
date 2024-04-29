# 동전 2 2294
"""
n : 동전의 종류 
k : 동전의 합 
동전의 수가 최소가 되도록 만들기, 동전 사용 개수는 상관없음 

입력 
(1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
출력 
사용한 동전의 최소 개수 , 불가능한 경우 -1

비교 : 그 전 목표값을 만들 수 있는 경우의 수 + 1 , 현재 목표값을 만들 수 있는 경우의수 

1 5 12 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
0 0 0 0 0 1 0 0 0 0 2  0  0  0  0  3
0 1 2 3 4 1 2 3 4 5 2  3  1  2  3  3
"""
# 왜 안되는거지
# import sys
# input = sys.stdin.readline
# n, k = map(int,input().split())
# coins = sorted([int(input()) for _ in range(n)])
# dp = [ 0 for _ in range(k+1) ]

# dp[coins[0]] = 1
# for i in range(coins[0],k+1,coins[0]):
#     dp[i] = dp[i-coins[0]] + 1


# for c in coins[1:]:
#     for i in range(c, k+1):
#         if dp[i-c] + 1 < dp[i]:
#             dp[i] = dp[i-c] + 1

# print(dp[k] if dp[k] else -1)


# ver 2
import sys
input = sys.stdin.readline
n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [100001 for _ in range(k+1) ]
dp[0] = 0

for c in coins:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c] + 1)

print(dp[k] if dp[k] != 100001 else -1)