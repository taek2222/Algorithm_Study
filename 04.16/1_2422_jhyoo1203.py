import sys
input = sys.stdin.readline

N, M = map(int, input().split())

not_comb = set()
for _ in range(M):
    a, b = map(int, input().split())
    not_comb.add((a, b))
    not_comb.add((b, a))
    
cnt = 0

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if (i, j) in not_comb:
            continue
        for k in range(j+1, N+1):
            if (i, k) in not_comb or (j, k) in not_comb:
                continue
            cnt += 1
            
print(cnt)