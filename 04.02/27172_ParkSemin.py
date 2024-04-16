'''
<백준 27172번 문제>
https://www.acmicpc.net/problem/27172

<개요>
카드는 1~1,000,000범위 내의 숫자를 가지며 각 숫자별 카드는
1개씩만 존재한다.
두 플레이어 A, B가 존재한다고 가정할 때, A의 카드로 B의 카드를
나눴을 때 나머지가 0이면 A의 승리이고 B의 패배, 둘다 아니라면 무승부다.
본인을 제외한 다른 모든 플레이어와 1번씩 결투를 하면 게임이 종료된다.

   **
   시간 제한이 1초, 즉 O(100,000,000)이므로 N의 최댓값인 100,000을
   기준으로 생각했을 때 O(10,000,000,000), 100초가 걸리므로 O(n^2)의
   시간복잡도를 가지고는 절대 풀 수 없다는 사실을 인지해야 한다.
   **
'''

# Ver 3)
# 1. 입력받기
n = int(input())
card_num = list(map(int, input().split()))

# 2. 점수를 저장할 score 배열을 미리 0으로 초기화
scores = [0] * 1000001

# 3. 1~1,000,000범위에서 등장한 카드의 숫자를 저장할 배열
used_num = [False] * 1000001
for i in card_num:
    used_num[i] = True

# 4. 각 경우마다 배수가 몇 개 있는지 확인
for num in card_num:
    # 현재 카드의 배수를 탐색
    for j in range(num*2, 1000000+1, num):
        # 이 숫자가 플레이어의 카드에 등장한 숫자인지 확인
        if used_num[j]:
            scores[num] += 1
            scores[j] -= 1

# 5. 출력
for i in card_num:
    print(scores[i], end=' ')

'''
# Ver 2)
# 1. 입력받기
n = int(input())
card_num = list(map(int, input().split()))

# 2. 점수를 저장할 score 배열을 미리 0으로 초기화
score = [0] * n

# 3. 각 경우마다 자신보다 인덱스가 큰 값이랑만 비교(중복하여 비교하는 경우를 제외함)
for i in range(n-1):
    for j in range(i+1, n):
        if card_num[j]%card_num[i] == 0:
            score[i] += 1
            score[j] -= 1

# 4. 출력
for i in score:
    print(i, end=' ')

# 그러나 이 코드 역시 O(n)*O(n-1)=O(n^2)의 시간복잡도를 가지므로
# 시간초과가 발생했다...
'''

'''
# Ver 1)
# 1. 입력받기
n = int(input())
card_num = list(map(int, input().split()))

# 2. 모든 플레이어가 서로 결투를 이루고 점수는 score에 저장
score = []
for i in range(n): # O(n)
    temp_score = 0
    for j in card_num: # O(n)
        # 자기 자신을 제외하고 결투
        if card_num[i] == j:
            continue

        if j % card_num[i] == 0:
            temp_score += 1
        elif card_num[i] % j == 0:
            temp_score -= 1
    score.append(temp_score)

# 3. 각 플레이어의 점수를 공백으로 구분하여 출력
for i in score:
    print(i, end=' ')

# 위 코드는 O(n^2)의 시간 복잡도를 가진다.
# N = 100,000이라면 시간 복잡도는 O(10,000,000,000)이다.
# 이 코드는 역시나 시간 초과가 떴다.
'''