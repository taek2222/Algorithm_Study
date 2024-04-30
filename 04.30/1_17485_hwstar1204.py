# 진우의 달 여행(Large) 17485
"""
N X M : 지구와 우주사이의 행렬 공간
행렬값 : 소모 연료의 양

우주선 이동 조건
    아래, 아래 왼쪽, 아래 오른쪽 
    같은 방향으로 두번 움직일 수 없음 
목표
    연료를 최대한 아끼면서 지구의 어느 위치에서든 출발하여 달의 어느 위치든 도착
    -> 최소 연료값 계산 
입력
    N, M (2 ≤ N, M ≤ 1000)
    행렬의 원소값 (100이하의 자연수)
"""

# import sys
# from collections import deque
# input = sys.stdin.readline

# n,m = map(int,input().split())
# # board = [list(map(int,input().split())) for _ in range(n)]

# board = [[0]*m for _ in range(n+1)]
# for i in range(1,n+1):
#     board[i] = list(map(int,input().split()))


# dx = [1,1,1]
# dy = [-1,0,1]
# visited = [[1000001]*m for _ in range(n+1)]
# visited[0] = [1] * m

# def BFS(sx,sy):
#     queue = deque()
#     queue.append((sx,sy))
#     visited[sx][sy] = board[sx][sy]

#     while queue:
#         # 현재 위치에서 다음 갈수 있는 위치
#         # 이전 방향이랑 다른 위치는 큐에 추가 X (board에서 현재 위치값+ 현재위치-현재 이동한거 반대로뺐을때의 위치값 == visited에서 현재 위치값 )이면 같은 방향임
#         # 범위내 이어야함 
#         # 다음 방문위치(visited)에 현재연료값 + 다음 위치 연료값 VS 그 위치의 연료값

#         nx, ny = queue.popleft()
#         for x,y in zip(dx,dy):
#             mx = nx+x
#             my = ny+y
            
#             if ny-y < 0 or ny-y >= m:
#                 print("mx: ",mx,"my: ",my)

#                 visited[mx][my] =  min(visited[mx][my] , board[mx][my] + visited[nx][ny])# 새로운 최소비용 저장
#                 queue.append((mx,my))
#                 continue
            
            
#             if mx >= n:
#                 continue  # 달 도착 

            
#             if 0 <= my < m:  # 행렬 범위 내
#                 if visited[nx][ny] != board[nx][ny] + visited[nx-x][ny-y]: # 다른 방향 
#                     visited[mx][my] = min(visited[mx][my] , board[mx][my] + visited[nx][ny])
#                     queue.append((mx,my))


# BFS(3,1)
# # 10 11 12 13 14 15
# print('...')
# for b in visited:
#     print(*b)



INF = 1000000
n, m = map(int, input().split())
fuels = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    for k in range(3):
        dp[0][j][k] = fuels[0][j]  # 첫번째 열 초기화 

for i in range(1, n):
    for j in range(m):
        for k in range(3):
            if (j == 0 and k == 0) or (j == m - 1 and k == 2):  # 1. 왼쪽 끝, 오른쪽 끝 (밖에서 안으로 들어오는 경우)
                dp[i][j][k] = INF
                continue
            if k == 0:   # 이전에 왼쪽에서 내려오는값이면 -> 이전에 중앙에서 내려오는값 vs 이전에 오른쪽에서 내려오는값
                dp[i][j][k] = fuels[i][j] + min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2])
            elif k == 1: # 이전에 중앙에서 내려오는값이면 -> 이전에 왼쪽에서 내려오는값 vs 이전에 오른쪽에서 내려오는값
                dp[i][j][k] = fuels[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])
            else:         # 이전에 오른쪽에서 내려오는값이면 -> 이전에 왼쪽에서 내려오는값 vs 이전에 중앙에서 내려오는값
                dp[i][j][k] = fuels[i][j] + min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])

result = INF
for j in range(m):
    result = min(result, min(dp[-1][j]))
print(result)

#https://velog.io/@iwtkmn0219/%EB%B0%B1%EC%A4%80-Python-17485%EB%B2%88-%EC%A7%84%EC%9A%B0%EC%9D%98-%EB%8B%AC-%EC%97%AC%ED%96%89-Large
