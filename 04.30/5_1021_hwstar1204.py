# 회전하는 큐 1021 
"""
n개의 원소를 포함하는 양방향 순환 큐 
3가지 연산 종류 
1. 첫번째 원소 뽑기 : 첫번째 원소 삭제됨
2. 왼쪽으로 한칸 이동 : 첫번째 원소가 마지막으로
3. 오른쪽 한칸 이동 : 마지막원소가 첫번째 원소로

n : 큐에 처음 포함되어 있던 수 
m : 뽑아내려고 하는 원소의 위치 

10 3
2 9 5

1 2 3 4 5 6 7 8 9 10  목표 : 1,8,4

0 1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9 0 (2)
2 3 4 5 6 7 8 9 0 (1)
0 2 3 4 5 6 7 8 9 (3)
9 0 2 3 4 5 6 7 8 (3)
8 9 0 2 3 4 5 6 7 (3)
9 0 2 3 4 5 6 7 (1)
7 9 0 2 3 4 5 6 (3)
6 7 9 0 2 3 4 5 (3)
5 6 7 9 0 2 3 4 (3)
4 5 6 7 9 0 2 3 (3)
5 6 7 9 0 2 3 (1)

"""
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())
target = list(map(int,input().split()))

queue = deque()
for i in range(1,n+1): # 1~n
    queue.append(i)

cnt = 0
for num in target:
    while True:
        t = queue.popleft()

        if t == num:
            break
        else:
            queue.appendleft(t)

        if queue.index(num) > len(queue)//2:  # 목표값의 인덱스가 처음 or 끝 어디쪽에 더 가까운지
            queue.appendleft(queue.pop())  # 3번연산
        else:
            queue.append(queue.popleft())  # 2번연산
        cnt += 1

    # 각 숫자마다 찾는 과정이 끝나면 queue의 상태 출력
    # print("Queue:", list(queue), "Cnt:", cnt)


print(cnt)


# # (1) 첫번쨰 원소 뽑기 
# queue.popleft()

# # (2) 왼쪽 이동
# queue.append(queue.popleft())

# # (2) 오른쪽 이동
# queue.appendleft(queue.pop())
