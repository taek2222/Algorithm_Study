# 경로찾기 11403
"""
가중치 없는 방향그래프 G
모든 정점 (i,j)에 대해서 i -> j로 가는 길이가 양수인 경로가 있는지 없는지 
입력
정점 개수 n (1 <= N <= 100)
그래프의 인접 행렬 
    1인 경우 : i->j로 가는 간선이 존재 
    0인 경우 : i->j로 가는 간선 없음 
    (i,i)는 모두 0 
출력
i -> j로 가는 길이 있으면 1 아니면 0 

BFS,DFS 그래프 탐색
"""

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def BFS(start):
    queue = deque()
    queue.append(start)

    check = [False for _ in range(n)]
    while queue:
        now = queue.popleft()

        for i in range(n):
            if not check[i] and graph[now][i]:
                queue.append(i)
                check[i] = True
                visited[start][i] = 1

for i in range(n):
    BFS(i)  # 모든 정점에서 출발

for v in visited:
    print(*v)

