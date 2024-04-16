'''
<베르트랑 공준>
1. n==2 : 2보다 크고 4보다 작은 소수 -> 3
2. n==3 : 3보다 크고 6보다 작은 소수 -> 5
3. n==4 : 4보다 크고 8보다 작은 소수 -> 5, 7
4. n==5 : 5보다 크고 10보다 작은 소수 -> 5, 7
5. n==6 : 6보다 크고 12보다 작은 소수 -> 7, 11

<조건>
시간 제한 : 1초
메모리 제한 : 256MB
1 <= n <= 123,456

<출력>
n < prime_num <= 2*n
'''
import sys
input = sys.stdin.readline # input() 함수를 readline으로 대체

# 1. 미리 소수 판별 리스트를 생성
bool_list = [True] * (123456*2 + 1)
for i in range(2, int((123456*2 + 1) ** 0.5)):
    if bool_list[i]:
        for j in range(i*2, 123456*2 + 1, i):
            bool_list[j] = False

# 2. 입력값이 0이 아닐 때까지 반복
while(n:=int(input())): # 바다코끼리 연산자 : 할당과 연산을 동시에 처리 
    print(len([i for i in range(n+1, 2*n+1) if bool_list[i]]))