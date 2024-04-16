'''
<입력>
- N : 홀수, 3 <= N <= 999
- M : 찾고자 하는 값, M <= N^2

<출력>
- 완성된 N*N의 2차원 배열
- M의 인덱스(단, 인덱스의 시작을 0이 아닌 1로 간주했을 때의 인덱스임

<해설>
- N*N크기의 2차원 배열에 1부터 N^2까지의 자연수를 달팽이 모양으로 채우는 문제
- arr[0][0] = N^2
- arr[N//2][N//2] = 1

---
<풀이 방법>
N=5일 때,
25 10 11 12 13
24  9  2  3 14
23  8  1  4 15
22  7  6  5 16
21 20 19 18 17
이다.

일단 [0][0]의 값을 N*N으로 설정하고 그후
아래로, 우측으로, 위로 각각 N-1번 이동하고
좌측으로는 (N-1)-1번 이동한다. 그리고 나서 
아래로 1칸 이동하여 값을 설정한다.

N=5이므로 처음에는 아래, 우측, 위로 각각 4번 이동한다.
그리고 좌측으로는 3번 이동한 뒤에 아래로 1칸 이동한다.
그때의 위치는 [1][1]이 된다.

다음으로는 아래, 우측 위로 각각 2번(4-2)번 이동한다.
좌측으로는 1번 이동한 뒤 아래로 1칸 이동한다.
그때의 위치는 [2][2]이고 값은 1이다.

이동하는 횟수가 2번이었으므로 이를 마지막 반복으로 보고 실행을 종료한다.
'''

# 1. 입력 받기
N = int(input())
M = int(input())
snail = [[0] * N for _ in range(N)]
k = N*N

# 2. 배열 채우기
row, column = 0, 0
snail[row][column] = k
k -= 1
for i in range(N-1, 1, -2): # if N==5, i => 4, 2
    for _ in range(i): # down
        row += 1
        snail[row][column] = k
        k -= 1
    
    for _ in range(i): # right
        column += 1
        snail[row][column] = k
        k -= 1

    for _ in range(i): # up
        row -= 1
        snail[row][column] = k
        k -= 1

    for _ in range(i-1): # left
        column -= 1
        snail[row][column] = k
        k -= 1

    row += 1 # down 1(set start-point)
    snail[row][column] = k
    k -= 1

# 3. 출력
for i in range(N):
    for j in range(N):
        print(snail[i][j], end=' ')
        if snail[i][j] == M:
            x, y = i, j
    print()

print(x+1, y+1)