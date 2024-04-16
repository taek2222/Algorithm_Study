# 행복 유치원
"""
n명의 원생들을 키 순서대로 일렬로 줄 세우고 k개의 조로 나눈다. 

조건
- 각 조에는 적어도 한명
- 각 조원들은 서로 인접해야함
- 조별로 인원수가 같을 필요는 없다. 

나눠진 조별로 단체 티셔츠를 맞춰야한다. 
티셔츠를 맞추는 비용: 조에서 max(키) - min(키)

입력 조건: 1 <= N <= 300,000  &  1 <= K <= M
목표: k개의 조별로 티셔츠 만드는 비용의 합의 최소

5 3 (n,k)
1 3 5 6 10      
x = 0 #몇명씩 자를지  

1. 똑같은 인원수로 최대한 나눠줘야하나?
TestCase: 
5 3
[1, 5, 11, 12, 13]
answer : 2 (1,1,3을로 나누었는데 최소값 나오는 테케)

2. 그럼 몇명씩 나눠줘야하지?
answer : 각 인원 키차이가 가장 많이 나는 순으로 조를 나눈다. 
diff = [4, 6, 1, 1] 
== [1 | 5 | 11 12 13]

3-1 가장 큰 값을 k-1개 0으로 만든 후 합 -> 시간초과  O(N^2)
3-2 가장 큰 값을 k-1개 삭제한 후 합-> 시간초과      O(N^2)
3-3 오름차순한 후 뒤에서 k-1개 뺀 합              O(NlogN)

TESTCASE
10 3
1 2 4 10 15 25 30 40 45 60

1 2 4 10 15 25 30 40 45 60 -> 29 5, 14 20  = 34
1 2 6 5 10 5 10 5 15 -> 가장 차이가 많이 나는 부분에서 k-1개 자르기

알고리즘 유형: Greedy Gold5
"""
# 3-1
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
p_list = list(map(int,input().split()))

diff = [0 for _ in range(n-1)]
for i in range(0,n-1):
    diff[i] = p_list[i+1] - p_list[i]

# k-1개만큼 가장 큰 값 제거 -> 시간 초과
for _ in range(k-1):
    diff.remove(max(diff)) 

print(sum(diff))



# 3-2
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
p_list = list(map(int,input().split()))

diff = [0 for _ in range(n-1)]
for i in range(0,n-1):
    diff[i] = p_list[i+1] - p_list[i]


#가장 큰 값을 0으로 만들기 -> 시간 초과
for _ in range(k-1):
    diff[diff.index(max(diff))] = 0 

print(sum(diff))


# 3-3
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
p_list = list(map(int,input().split()))

#각 인원간 비용
diff = [p_list[i+1] - p_list[i] for i in range(n-1)] 
#오름차순 정렬 
diff.sort()

print(sum(diff[:n-k])) # (n-1)-(k-1)개 빼고 