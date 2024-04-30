'''
https://www.acmicpc.net/problem/21758
<문제>
- N개(꿀통)의 1차원 리스트가 주어짐
- 벌은 2마리가 존재
- 주어진 N개의 꿀통에서 2마리의 벌이 딸 수 있는 꿀의 최댓값을 구하는 문제
  - 단, 벌들의 초기 위치에서는 꿀을 딸 수 없다.
  - 벌들은 오직 벌통 방향으로만 이동할 수 있다.

<입력>
- 첫째 줄: N(3 <= N <= 100,000) - 꿀통의 갯수
- 둘째 줄: N개의 정수 - 각 꿀통에 든 꿀의 양
'''

'''
<풀이 방향>
- 벌통과 벌의 간격이 최대한 멀어야지 많은 값을 더할 수 있다.
  case 1) 벌이 왼쪽 끝, 벌통은 오른쪽 끝(벌 한마리는 왼쪽에서 오른쪽으로 한칸씩 이동)
  case 2) 벌이 오른쪽 끝, 벌통은 왼쪽 끝(벌 한마리는 오른쪽에서 왼쪽으로 한칸씩 이동)
  case 3) 벌이 양쪽 끝, 벌통은 왼쪽에서 오른쪽으로 한칸씩 이동
  
- n의 최댓값이 100,000이므로 O(n^2)의 시간복잡도는 절대 있어선 안된다.
  - n번의 반복 한 번으로 최댓값을 찾도록 한다.
  - 한 번의 반복마다 위 3개의 경우를 모두 비교하여 최댓값을 정한다.
'''

# 1. 입력 받기
n = int(input())
honey = list(map(int, input().split()))
sum_honey = [honey[0]] # sum_honey[i]는 0부터 i까지의 부분 합을 뜻함
for i in range(n-1): # 초깃값을 1개 설정했으므로 n-1까지 반복
    sum_honey.append(sum_honey[i] + honey[i+1])

# 2. max를 설정하고 max보다 큰 값이 나오면 변경
total = 0
for i in range(1, n-1):
    total = max(total, sum_honey[n-1]-honey[0]-honey[i] + sum_honey[n-1]-sum_honey[i]) # 꿀통 맨 오른쪽 
    total = max(total, sum_honey[i-1] + sum_honey[n-2]-honey[i]) # 꿀통 맨 왼쪽
    total = max(total, sum_honey[i]-honey[0] + sum_honey[n-2]-sum_honey[i-1]) # 꿀통 가운데 범위

# 3. 출력
print(total)