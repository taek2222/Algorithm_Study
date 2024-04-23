# 배 1092
"""
크레인 n대 1분에 하나씩 배에 실어나르기 
조건
    모든 크레인은 동시에 움직임 
    크레인 무게제한 : 해당 무게 제한보다 무거운건 크레인으로 움직이지 못함
목표
    모든 박스를 배로 옮기는데 드는 시간의 최솟값 구하기

입력
    n : 크레인 개수 (0 < n <= 50)
    각 크레인의 무게제한 : < 1,000,000
    m : 박스의 수 (0 < m <= 10,000)
    각 박스의 무게  : < 1,000,000
출력
    모든 박스를 배로 옮기는데 드는 시간의 최솟값
    모든 박스를 배로 옮길 수 없으면 -1 

idea
1분 단위(모든 크레인을 확인하면서)로 옮기는 과정을 진행한다. 
무게제한이 큰 크레인부터 무거운 박스먼저 무게제한되지 않는 박스를 옮긴다. 

# 정렬 전
10
11 17 5 2 20 7 5 5 20 7
5
18 18 15 15 17

# 정렬 후
10
20 20 17 11 7 7 5 5 5 2
5
18 18 17 15 15

크레인 최대 50개 정렬
박스 최대 10,000개 정렬
"""
# 리스트 
import sys
input = sys.stdin.readline

n = int(input())
cranes = sorted(list(map(int,input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int,input().split())), reverse=True)
minuite = 0

if cranes[0] < boxes[0]:  # 모든 박스를 옮기지 못하는 경우 
    print(-1)
    exit()

cnt = 0
for c in cranes:
    if boxes[-1] <= c:  # 가장 가벼운 박스 보다 큰 무게제한을 가진 크레인
        cnt += 1
cranes = cranes[:cnt]  # 유효한 크레인 재정의 (반복 최적화)


while boxes:
    for crane in cranes:
        for box in boxes:
            if box <= crane:
                boxes.remove(box)
                break
    minuite += 1

print(minuite)

# 우선순위 큐 -> 실패..
# import sys
# from queue import PriorityQueue
# input = sys.stdin.readline

# n = int(input())
# cranes = sorted(list(map(int,input().split())))
# m = int(input())
# boxes = list(map(int,input().split()))

# cnt = 0
# for c in cranes:
#     if c < min(boxes):
#         cnt += 1
# cranes = cranes[cnt:]
# # print(cranes)
# # print(min(boxes))

# if cranes[-1] < max(boxes):  # 모든 박스를 옮기지 못하는 경우 
#     print(-1)
#     exit()

# pq = PriorityQueue() # 박스 무게 우선순위 큐
# for box in boxes:
#     pq.put(box)

# minuite = 1
# used = [False] * n  # 사용한 크레인 체크
# check = 0



# while not pq.empty():
#     box = pq.get()  # 가장 가벼운 박스 무게 

#     if check == len(cranes):  # 1분에 사용하는 크레인 수 채워지면
#         check = 0
#         used = [False] * n
#         minuite += 1

#     for i, c in enumerate(cranes):
#         if box <= c and not used[i]:  # 박스옮길 크레인 찾음 
#             used[i] = True
#             break
#     check += 1
    
# print(minuite)


import sys
input = sys.stdin.readline

n = int(input())
cranes = sorted(list(map(int,input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int,input().split())), reverse=True)
minuite = 0

if cranes[0] < boxes[0]:  # 모든 박스를 옮기지 못하는 경우 
    print(-1)
    exit()

cnt = 0
for c in cranes:
    if boxes[-1] <= c:  # 가장 가벼운 박스 보다 큰 무게제한을 가진 크레인
        cnt += 1
cranes = cranes[:cnt]  # 유효한 크레인 재정의 


while boxes:
    for crane in cranes:
        for box in boxes:
            if box <= crane:
                boxes.remove(box)
                break
    minuite += 1

print(minuite)
