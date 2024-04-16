'''
<해설>
N종류의 아이스크림 중에서 3가지 아이스크림을 선택하는 방법

<입력>
N(1<=N<=200): 아이스크림의 종류
M(0<=M<=10000): 섞어먹으면 안되는 조합의 개수
이후 M개의 줄: 섞어먹으면 안되는 조합
<출력>
가능한 방법의 총 개수


1 2 3 4 5

1 2 3 [1, 2]
1 2 4 [1, 2]
1 2 5 [1, 2]
1 3 4 [1, 3]
1 3 5 [1, 3]
1 4 5

2 3 4 [3, 4]
2 3 5 
2 4 5

3 4 5 [3, 4]

'''

# ver 2(set 활용) - 메모리 초과
'''
import sys
imput = sys.stdin.readline

# 1. 입력 받기
N, M = map(int, input().split())
mix = []
for _ in range(M):
    mix.append(set(map(int, input().split())))

# 2. 가능한 모든 조합을 possible에 추가
possible = []
for i in range(1, N-1): # O(200*200*200) = O(8,000,000)
    for j in range(i+1, N):
        for k in range(j+1, N+1):
            possible.append({i, j, k})

# 3. 섞어 먹을 수 없는 조합은 카운트에서 감소
cnt = len(possible)
for case in possible: # O(200*10,000) = O(2,000,000)
    for m in mix:
        if set(case).intersection(m) == m:
            cnt -= 1
            break

print(cnt)
'''

# ver 1 - 31120KB, 620ms
import sys
input = sys.stdin.readline

# 1. 입력 받기
N, M = map(int, input().split())
mix = [[]] * (N+1) # 인덱스와 값을 일치시키기 위해 +1
for _ in range(M):
    temp = sorted(map(int, input().split()))
    # 조합이 [1, 2]라면 mix[1]에 2를 추가함. [1, 3]이 추가되면 mix[1] = [2, 3]
    mix[temp[0]] = mix[temp[0]] + [temp[1]] 

# 2. 하나씩 3개의 숫자를 조합해보면서 3개의 숫자가 섞어먹으면 안되는 조합일 경우 continue, 된다면 개수 1 증가
cnt = 0
for i in range(1, N-1):
    for j in range(i+1, N):
        if j in mix[i]:
            continue
        for k in range(j+1, N+1):
            if k in mix[i] or k in mix[j]:
                continue
            else:
                cnt += 1

print(cnt)