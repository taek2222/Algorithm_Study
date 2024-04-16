# 함계 블록 쌓기 18427
"""
1~n 학생들은 최대 m개의 블록을 가지고 있음 
차례대로 블록을 쌓으면서 정확히 높이가 h인 탑 만들수 있는 경우의 수 

조건
    블록을 사용하지 않아도 됨
    한 학생당 최대 1개의 블록 사용 가능 
    
입력
    (1 ≤ N ≤ 50, 1 ≤ M ≤ 10, 1 ≤ H ≤ 1,000)
    한 명의 학생이 가지고 있는 모든 블록들의 높이는 서로 다르게 주어진다.

idea
1~n 학생들 차례대로 쌓을 수 있는 탑의 경우의 수 업데이트 
h를 넘지 않는 선에서 이전 학생이 쌓은 경우의 수를 고려해야함 
"""
import sys
input = sys.stdin.readline
n,m,h = map(int,input().split())

dp = [[0 for _ in range(h+1)] for _ in range(n+1)]
blocks = [list(map(int,input().split())) for _ in range(n)]  # 학생들 블록목록

# init 1
for i in range(0, n+1):
    dp[i][0] = 1
# init 2
for b in blocks[0]:
    dp[1][b] = 1



for i in range(2,n+1):  # 2번째 학생부터
    for j in range(1,h+1):  # 1~h 높이까지 

        for block_height in blocks[i-1]: # 해당 라인에 학생이 가진 블록을 탐색
            before = j-block_height      # 높이 - 학생이 가진 블록 높이 
            if before >= 0:  # and dp[i-1][before] != 0
                dp[i][j] += dp[i-1][before]
        
        dp[i][j] += dp[i-1][j]  # 이전에 기억한 값 사용 

# for d in dp:
#     print(*d)

print(dp[-1][-1] % 10007)