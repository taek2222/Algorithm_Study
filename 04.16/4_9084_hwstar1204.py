# 동전 9084
"""
입력
testcase 개수 : T (1 ≤ T ≤ 10)
동전 종류 :  N (1 ≤ N ≤ 20)
N가지 동전 오름차순 정렬 
N가지 동전으로 만들어야하는 금액 : M (1 ≤ M ≤ 10000)

출력
각 testcase에 대해 n가지 동전으로 M 금액을 만드는 모든 방법의 수 하나씩

testcase : 3원,4원 => 15원
   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
3원 1 0 0 1 0 0 1 0 0 1 0  0  1  0  0  1
4원 1 0 0 1 1 0 1 1 1 1 1  1  2  1  1  2

15 = [ 3*5, 4*3+3 ] = 2가지

"""
# ver1
# import sys
# input = sys.stdin.readline
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     coins = list(map(int,input().split()))
#     target = int(input())

#     dp = [ 0 for _ in range(target + 1)]
#     dp[0] = 1  # 0원 만드는 경우의 수 

#     for c in coins:
#         for i in range(target+1):
#             if dp[i] and (i+c <= target):  # 미래에 가능할때 현재값을 가지고 업데이트
#                 dp[i+c] += dp[i]
    
#     print(dp[target])



# ver2
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int,input().split()))
    target = int(input())

    dp = [ 0 for _ in range(target + 1)]
    dp[0] = 1  # 0원 만드는 경우의 수 

    for c in coins:
        for i in range(c, target+1):  # 현재까지 가능할때 과거 데이터를 가지고 업데이트
            dp[i] += dp[i-c]
    
    print(dp[target])