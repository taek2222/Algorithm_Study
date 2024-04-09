import sys
input = sys.stdin.readline

MAX = 123456
prime = [1 for _ in range(MAX*2+1)]
prime[0] = 0
prime[1] = 0

for i in range(2, MAX*2+1):
    if prime[i]:
        for j in range(i*2, MAX*2+1, i):
            prime[j] = 0

while True:
    n = int(input())
    if not n:
        break
    print(sum(prime[n+1 : n*2 + 1]))    