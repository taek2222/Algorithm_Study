# 센서 2212 
"""
n개의 센서가 적어도 하나의 집중국과 통신하면서 수신 가능 영역 길이의 합 최소화 
센서는 원점으로 부터 정수거리 위치 (좌표: 정수하나)
-> 각 집중국의 수신 가능 영역의 거리의 합의 최소값 구하기 
** 수신 가능 영역 길이는 0이상
입력
센서 개수 : N (1 <= N <= 10,000)
집중국 개수 : K (1 <= K <= 1,000)
N개의 센서 좌표 (절대값 <= 1,000,000)

idea 
1. 집중국은 최대한 많을수록 연결 거리를 줄일수 있으므로 다 사용한다. 
2. 집중국의 위치 후보는 센서의 위치들이다. (거리가 0이어도 됨)
3. 각 센서간의 거리 차이가 가장 작은 순서대로 k-n개 뽑아서 더한다. 

# testcase1 
1 3 6 6 7 9
  v     v 
2 3 0 1 2  
n-k개 최솟값 = 0+1+2+2 = 5 

# testcase2 
3 6 7 8 10 12 14 15 18 20 
  v     v v   v     v
0 3 1 1 2 2   2  1  3  2
n-k개 최솟값 = 0+1+1+1+2+2 = 7
"""
import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
sensers = sorted(list(map(int,input().split())))  # 센서 위치 & 정렬

min_len = [0] * (n-1)  # 센서 사이 거리 리스트 업데이트 & 정렬
for i in range(n-1):
    min_len[i] = sensers[i+1] - sensers[i]
min_len.sort()
# min_len = sorted([sensers[i+1] - sensers[i] for i in range(n-1)]) 

print(sum(min_len[:n-k]))  # 센서 거리 가장 작은순으로 n-k개의 합