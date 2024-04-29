import sys
input = sys.stdin.readline

N = int(input().rstrip())
file = {}

for _ in range(N):
    filename = input().rstrip().split('.')
    
    if filename[1] in file:
        file[filename[1]] += 1
    else:
        file[filename[1]] = 1

file = sorted(file.items(), key = lambda x:x[0], reverse=False)

for i in file:
    print(i[0], i[1])