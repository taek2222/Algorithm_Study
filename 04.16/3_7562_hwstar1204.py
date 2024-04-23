# 나이트의 이동 7562
"""
체스판 위에 나이트가 이동하려는 칸이 주어질 때 몇번 움직이면 이칸으로 이동할 수 있는지 
입력
testcase 개수 
    첫째줄: 체스판 한변의 길이 l -> 체스판 크기 l*l  (0~l-1)*(0~l-1)  조건 : (4<=l<=300)
    둘째줄: 나이트가 현재 있는 칸 (now_x, now_y)
    셋째줄: 나이트가 이동하려는 칸 (target_x, target_y)

출력
    각 testcase마다 최소 몇번만에 이동할 수 있는지 출력 
"""
from collections import deque
import sys
input = sys.stdin.readline

dx = (2,1,-1,-2,-2,-1,1,2)
dy = (1,2,2,1,-1,-2,-2,-1)

def check(i,j):  
    return (0 <= i < board) and (0 <= j < board)

def BFS(nx,ny):
    queue = deque()
    queue.append((nx,ny))
    visited[nx][ny] = 1  # 방문 표시 때문에 1부터 시작
    
    while queue:
        now_x, now_y = queue.popleft()

        if (now_x == tx and now_y == ty):
            return visited[now_x][now_y] - 1

        for x,y in zip(dx,dy):
            moved_x = now_x + x
            moved_y = now_y + y
            if check(moved_x,moved_y):  # 범위 확인        
                if not visited[moved_x][moved_y]:
                    visited[moved_x][moved_y] = visited[now_x][now_y] + 1  # 그 전까지 이동한 거리 +1
                    queue.append((moved_x,moved_y))


n = int(input())

for _ in range(n):
    board = int(input())
    nx, ny = map(int,input().split())  # 현재 위치
    tx, ty = map(int,input().split())  # 목표 위치 
    visited = [[0]*board for _ in range(board)]
    
    answer = BFS(nx,ny)
    print(answer)