'''
<코드 해설>
나이트가 이동할 수 있는 경우는 
(2, 1)
(2, -1)
(1, 2)
(1, -2)
(-2, 1)
(-2, -1)
(-1, 2)
(-1, -2)
의 총 8가지가 있다.

체스판의 크기인 l*l에 해당하는 2차원 배열(초깃값: 0)을 선언하고
나이트의 현재 위치에 해당하는 인덱스의 값을 1로 설정한다.

이후 나이트가 이동하면서 방문하는 좌표의 값을
'이전 위치에서의 2차원 배열 값에 1을 더한 값'으로 설정한다.

나이트는 총 8가지의 경우로 이동할 수 있으므로 각 경우 별 나이트가 
이동할 수 있는 모든 좌표의 경우를 다 확인한다. 단, 나이트는 체스판의
범위를 벗어나면 안되므로 체스판의 범위를 벗어나는 경우는 continue를
사용하여 건너뛰도록 한다.

나이트가 방문하는 좌표를 queue에 추가하고 반복을 할 때마다 pop하여
나이트가 방문한 각 좌표의 8가지 경우의 수를 모두 따져보며 실행을 반복하다가
방문한 좌표가 목표 좌표일 경우에 해당 좌표의 인덱스에 해당하는 2차원 배열의 값,
즉 이동한 횟수를 출력하고 현재 테스트 케이스의 실행을 종료한다.
'''

from collections import deque

x = [+2, +2, +1, +1, -2, -2, -1, -1]
y = [+1, -1, +2, -2, +1, -1, +2, -2]

def bfs(now_x, now_y, aim_x, aim_y):
    queue = deque()
    queue.append((now_x, now_y))

    while queue:
        curX, curY = queue.popleft()

        # 나이트가 방문한 좌표가 목표 좌표인지 확인
        if curX == aim_x and curY == aim_y:
            # 처음 시작 경로의 탐색 수를 1로 설정하고 시작했으므로 마지막에 1을 다시 빼줌
            print(visited[curX][curY] - 1)
            return

        # 나이트의 이동 경우의 수인 8가지를 모두 탐색
        for i in range(8):
            move_x = curX + x[i]
            move_y = curY + y[i]
            
            # 나이트가 이동한 위치가 체스판의 범위를 벗어나는지 확인
            if move_x < 0 or move_x >= l or move_y < 0 or move_y >= l:
                continue

            # 체스판 범위 내라면 해당 좌표까지 이동한 횟수를 추가하고
            # 큐에 나이트가 방문한 좌표를 추가
            if visited[move_x][move_y] == 0:
                visited[move_x][move_y] = visited[curX][curY] + 1
                queue.append((move_x, move_y))


N = int(input())
for i in range(N):
    l = int(input())
    visited = [[0] * l for _ in range(l)]

    now_x, now_y = map(int, input().split())
    aim_x, aim_y = map(int, input().split())

    visited[now_x][now_y] = 1
    bfs(now_x, now_y, aim_x, aim_y)