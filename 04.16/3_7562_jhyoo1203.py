from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(t):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    x, y = map(int, input().split())
    rx, ry = map(int, input().split())
    
    q = deque()
    q.append((x, y))
    graph[x][y] = 1
    
    while q:
        x, y = q.popleft()
        if x == rx and y == ry:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not graph[nx][ny]:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    print(graph[rx][ry]-1)