import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
coordinate = list(map(int, input().split()))
coordinate.sort()

temp = []
for i in range(1, N):
    temp.append(coordinate[i] - coordinate[i-1])
temp.sort()

print(sum(temp[:N-K]))