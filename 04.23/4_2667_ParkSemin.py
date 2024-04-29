'''
https://www.acmicpc.net/problem/2667

<문제>
- N*N 크기의 지도가 입력
- 상,하,좌,우가 연결되어있는 구역이 하나의 단지가 됨
- 전체 지도의 단지 수를 출력하고 각 단지 내 집의 수는 오름차순으로 출력
- 지도가 나왔으니 탐색 알고리즘

<입력>
- 첫째 줄 : N(5 <= N <=25) - 정사각형 지도 한 변의 길이

<출력>
- 첫째 줄 : 전체 단지의 수(K)
- K개 줄 : 각 단지 내 집의 수를 오름차순 정렬하여 출력
'''

'''
<풀이 방향>
1. map[0][0]부터 탐색 시작
2. 1을 만나면 방문 표시를 하고 상, 하, 좌, 우에 또 다른 1이 있는지 탐색하여
   있으면 큐에 추가하고 없으면 넘어감
3. 이렇게 탐색이 끝나고 더 이상 연결된 1이 없다면 현재까지의 집의 수를 리스트에 추가
'''

from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    cnt = 1
    while queue:
        now_x, now_y = queue.popleft()

        # 현재 위치에서 상, 하, 좌, 우로 이동
        for k in range(4):
            move_x = now_x + dx[k]
            move_y = now_y + dy[k]

            # 이동한 범위가 맵 내부인 경우에만 실행
            if 0 <= move_x < n and 0 <= move_y < n:
                # 이미 방문한 곳이면 넘어감
                if map[move_x][move_y] == '1':
                    # 방문 표시 + 큐에 추가 + 집 개수 1 증가
                    map[move_x][move_y] = 'X'
                    queue.append((move_x, move_y))
                    cnt += 1

    #❌ # cnt == 0이라면 자기 자신만 1인 것이므로 단지가 아님
    #❌ if cnt != 0: town.append(cnt+1)
    
    # 문제에서 '단지'란 '연결된 집의 모임'이라 하였고, 연결되었다는 것은 어떤 집이
    # 상하좌우로 있는 것을 말한다고 했다. 즉, 하나의 집은 단지가 아니라고 생각하여 넘어갔으나
    # 테스트 케이스를 보다보니 하나의 집도 단지로 치는 것 같다.
    town.append(cnt)


# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 1. 입력
n = int(input())
map = [ list(input().rstrip()) for _ in range(n) ]

# 2. bfs
town = []
for i in range(n):
    for j in range(n):
        if map[i][j] == '1':
            map[i][j] = 'X' # 초기 위치 방문 표시
            bfs(i, j)

# 3. 출력
print(len(town)) # 전체 단지의 수
for i in sorted(town):
    print(i) # 각 단지 별 집의 수