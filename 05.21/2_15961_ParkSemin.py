'''
https://www.acmicpc.net/problem/15961

<입력>
- N(2 <= N <= 3,000,000) - 벨트에 놓인 접시의 수
- d(2 <= d <= 3,000) - 초밥의 가짓 수
- k(2 <= k <= 3,000, k<=N) - 연속해서 먹는 접시의 수
- c(1 <= c <= d) - 쿠폰 번호
- 이후 N개의 줄: N개 접시에 놓인 초밥 N개의 번호

<출력>
- 주어진 회전 초밥 벨트에서 먹을 수 있는 초밥의 가짓수의 최댓값
'''

# 1. 입력
from collections import deque, defaultdict
import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

# 2. 초기 설정
current_sushi = defaultdict(int)
current_unique = 0
deq = deque()

# 2-1. 초기 슬라이딩 윈도우 설정
for i in range(k):
    deq.append(sushi[i])
    if current_sushi[sushi[i]] == 0:
        current_unique += 1
    current_sushi[sushi[i]] += 1

# 2-2. 쿠폰 초밥 추가 고려
max_unique = current_unique
if current_sushi[c] == 0:
    max_unique += 1

# 3. 슬라이딩 윈도우 탐색
for i in range(n):
    # 최댓값은 k+1이므로 최댓값을 찾았다면 반복 종료
    if max_unique == k+1: break

    # 슬라이딩 윈도우에서 초밥 제거
    remove_sushi = deq.popleft()
    current_sushi[remove_sushi] -= 1
    if current_sushi[remove_sushi] == 0:
        current_unique -= 1

    # 슬라이딩 윈도우에 초밥 추가
    add_sushi = sushi[(i + k) % n]
    deq.append(add_sushi)
    if current_sushi[add_sushi] == 0:
        current_unique += 1
    current_sushi[add_sushi] += 1

    # 쿠폰 초밥이 포함되지 않았다면 추가, 포함되었다면 최댓값만 비교
    max_unique = max(max_unique, current_unique + 1) if current_sushi[c] == 0 else max(max_unique, current_unique)

# 4. 출력
print(max_unique)