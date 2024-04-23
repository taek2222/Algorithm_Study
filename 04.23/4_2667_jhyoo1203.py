from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = []


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    count = 1
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(i, j))

cnt.sort()

print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
