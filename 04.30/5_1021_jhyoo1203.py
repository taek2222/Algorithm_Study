from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
idx = list(map(int, input().split()))

dq = [i for i in range(1, N + 1)]
res = 0

for i in range(M):
	for j in range(len(dq)):
		if idx[i] == dq[j]:
			break
	if j <= len(dq) / 2:
		while idx[i] != dq[0]:
			dq.append(dq.pop(0))
			res += 1
	else:
		while idx[i] != dq[0]:
			dq.insert(0, dq.pop())
			res += 1
	dq.pop(0)
 
print(res)