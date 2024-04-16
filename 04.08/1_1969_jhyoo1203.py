import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = [input().rstrip() for _ in range(n)]
type = ['A', 'C', 'G', 'T']
res = ''
hd = 0

for i in range(m):
    cnt = [0, 0, 0, 0]
    for j in range(n):
        if dna[j][i] == type[0]:
            cnt[0] += 1
        elif dna[j][i] == type[1]:
            cnt[1] += 1
        elif dna[j][i] == type[2]:
            cnt[2] += 1
        elif dna[j][i] == type[3]:
            cnt[3] += 1
    
    idx = cnt.index(max(cnt))
    if idx == 0:
        res += type[0]
    elif idx == 1:
        res += type[1]
    elif idx == 2:
        res += type[2]
    elif idx == 3:
        res += type[3]
    hd += n - max(cnt)

print(res)
print(hd)