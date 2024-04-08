# 최소 회의실 개수 19598
"""
n개의 회의를 모두 진행할 수 있는 최소 회의실 개수 구하기 (Greedy)

입력
n : 회의실 개수 (1 <= N <= 100,000) -> 최소 O(nlogn)정도의 알고리즘 필요
시작시간, 종료시간

testcase
6
0 20 
10 20  
0 40
10 40 
20 40
30 50
"""

# ver 2 O(nlogn)
import sys
import heapq
input = sys.stdin.readline
n = int(input())

times = [tuple(map(int,input().split())) for _ in range(n)]
times.sort()  # 시작시간 작은순 정렬

heap = []
heapq.heappush(heap,times[0][1])  # 비교를 위해서 첫번째 회의 시간 추가 
cnt = 1

for i in range(1,n):
    if heap[0] <= times[i][0]:  # 우선순위 회의의 끝나는 시간 <= 새로운 회의의 시작 시간 
        heapq.heappop(heap)     # 회의를 이어서 하는 경우
    else:
        cnt += 1                # 새로운 회의실에서 회의하는 경우
    heapq.heappush(heap, times[i][1]) 

print(cnt)

#------------------------------------------------------------------------

# ver 1 O(n^2)

# import sys
# input = sys.stdin.readline
# n = int(input())

# times = [tuple(map(int,input().split())) for _ in range(n)]
# times.sort(key=lambda x: (x[1],x[0]))  # 종료시간, 시작시간 작은순 정렬

# min_times = [(0,0)]  # 최소 dummy 값 추가 
# for t in times:
#     for i, min_t in enumerate(min_times):   
#         if min_t[1] <= t[0]:      # 저장해놓은 회의 종료시간보다 크거나 같은 회의 시작시간을 이어서 회의
#             min_times[i] = t
#             break
#     else:
#         min_times.append(t)       # 그런 경우가 없으면 새로운 회의실 추가 

# print(len(min_times))


#------------------------------------------------------------------------

# ver 3 O(n^2이지만 ver1보다는 개선됨)
# 시작시간으로 오름차순 정렬된 list를 queue로 만들어서 
# 빠른 시작 시간 회의순서대로 종료시간뒤에 이어질 회의가 있으면 통과 아닌경우 회의실개수 +1
# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())

# queue = deque(sorted(tuple(map(int, input().split())) for _ in range(n)))

# cnt = 0
# for i in range(n-1):
#     now = queue.popleft()  # ver1보다 개선된 부분
#     for j in range(i+1,len(queue)):
#         if now[1] <= queue[j][0]:
#             break
#     else:
#         cnt += 1

# print(cnt)
