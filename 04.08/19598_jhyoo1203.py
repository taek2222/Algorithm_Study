import sys, heapq
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort()
h = []

for start, end in data:
    if h and h[0] <= start:
        heapq.heappop(h)
    heapq.heappush(h, end)

print(len(h))