import sys
input = sys.stdin.readline


N, d, k, c = map(int, input().split())

sushi = []
for _ in range(N):
    sushi.append(int(input()))

dish = [0 for _ in range(d+1)]

count = 0
for i in range(k):
    if dish[sushi[i]] == 0:
        count += 1
    dish[sushi[i]] += 1

    if dish[c] == 0:
        answer = count + 1
    else:
        answer = count


for i in range(k, N + k - 1):
    if dish[sushi[i % N]] == 0:
        count += 1
    dish[sushi[i % N]] += 1

    if dish[sushi[i - k]] == 1:
        count -= 1

    dish[sushi[i - k]] -= 1

    if dish[c] == 0:
        answer = max(answer, count + 1)
    else:
        answer = max(answer, count)

print(answer)