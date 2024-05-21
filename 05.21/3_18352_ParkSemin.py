'''
https://www.acmicpc.net/problem/18352

<입력>
- N(2 <= N <= 300,000) - 도시의 개수
- M(1 <= M <= 1,000,000) - 도로의 개수
- K(1 <= K <= 300,000) - 최단 거리의 정보
- X(1 <= X <= N) - 출발 도시의 번호
- 이후 M개의 줄: 자연수 A, B(1 <= A,B <= N, A != B) - A번 도시에서 B번 도시로 이동하는 도로가 존재한다는 뜻

<출력>
- X로부터 출발하여 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순 정렬하여 출력
- 최단 거리가 K인 도시가 하나도 존재하지 않는다면 -1 출력

<풀이>
- 모든 경로를 방문하며 최단 경로를 찾아서 저장 => 탐색이니 그래프 알고리즘 사용, 저장해야하니 배열 사용
'''

# 1. 입력
from collections import defaultdict, deque
import math
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
visit = [False] * (N+1)
route = defaultdict(list)
for _ in range(M):
    key, value = map(int, input().split())
    route[key].append(value)

# 2. 최단 거리를 저장할 배열 선언
result = [math.inf] * (N+1)
result[X] = 0

# 3. 최단 거리 탐색 알고리즘
move = deque()
move.append(X)
while move:
    start_node = move.popleft()
    visit[start_node] = True
    for end_node in route[start_node]:
        if not visit[end_node]: move.append(end_node)
        
        if result[end_node] > result[start_node] + 1:
            result[end_node] = result[start_node] + 1

# 4. 출력
answer = []
for i in range(1, N+1):
    if result[i] == K:
        answer.append(i)
if answer:
    for i in answer:
        print(i)
else:
    print(-1)

'''
@ 1 1 @

@ 1 1 1
@ @ @ @
@ @ @ @
@ @ @ @

@ 1 1 2
@ @ 1 1
@ @ @ @
@ @ @ @
'''