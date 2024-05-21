from collections import deque
import sys
input = sys.stdin.readline


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(x, k):
    res = []
    q = deque([x])
    visited[x] = True
    
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                distance[i] = distance[x] + 1
                
                if distance[i] == k:
                    res.append(i)
        
    if len(res) == 0:
        print(-1)
    else:
        res.sort()
        for i in range(len(res)):
            print(res[i])


bfs(x, k)