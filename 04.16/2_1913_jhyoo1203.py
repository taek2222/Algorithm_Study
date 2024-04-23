import sys
input = sys.stdin.readline

N = int(input())
find = int(input())
graph = [[0]*N for _ in range(N)]

x, y = N//2, N//2
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = 1
rx, ry = 0, 0
graph[x][y] = n
n += 1
if find == 1:
    rx, ry = N//2 + 1, N//2 + 1

for i in range(1, N//2 + 1):
    if n == 2:
        nx, ny = x-1, y-1
    else:
        nx, ny = nx-1, ny-1
    
    step = i*2
    for j in range(4):
        for k in range(step):
            nx = nx + dx[j]
            ny = ny + dy[j]
            graph[nx][ny] = n
            if n == find:
                rx, ry = nx+1, ny+1
            n += 1

for val in graph:
    print(*val)
print(rx, ry)