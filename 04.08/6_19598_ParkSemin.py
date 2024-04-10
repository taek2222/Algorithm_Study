'''
<해설>
- 한 회의실에서 동시에 두 개 이상의 회의 진행 불가
- 한번 시작된 회의는 중간에 중단되지 않으며 회의가 끝남과 동시에 다음 회의 진행 가능

<입력>
- 회의의 개수(1<=N<=100,000) => O(n^2)은 불가능함
- 시작시간, 종료시간 : 2^31-1보다 작거나 같은 자연수 또는 0

<출력>
- 최소 회의실 개수

<키포인트>
- 시간복잡도를 줄여야 함
'''

import sys
import heapq
input = sys.stdin.readline

# 1. 입력 받기
n = int(input())
time = sorted([list(map(int, input().split())) for _ in range(n)])
room = []

# 2. 구현(우선 순위 큐를 위한 자료구조인 heap을 안쓰고 시간복잡도를 만족할 수 있는 방법이 있나..?)
for start, end in time:
    if room and room[0] <= start:
        heapq.heappop(room)

    heapq.heappush(room, end)    

print(len(room))