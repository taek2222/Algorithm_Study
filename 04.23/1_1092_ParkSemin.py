'''
https://www.acmicpc.net/problem/1092

<문제>
크레인 N대 있음.
각 크레인은 무게 제한을 가짐.
크레인은 1분에 1개씩 박스를 배에 실을 수 있음. 
모든 크레인은 동시에 움직임.
만약 모든 박스를 배로 옮길 수 없으면 -1을 출력
=> 모든 박스를 배로 옮기는데 드는 시간의 최솟값 구하기

<입력>
- 첫째 줄: n(1<=N<=50) - 총 크레인의 수
- 둘째 줄: crane_weight[] - 각 크레인의 무게 제한(전체 N개)
- 셋째 줄: m(1<=M<=10,000) - 총 박스의 수
- 넷째 줄: box_weight[] - 각 박스의 무게 제한(전체 M개)

<출력>
- 모든 박스를 배로 옮기는데 드는 시간의 최솟값
- 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력🔴🔴

==============

<예제 입력 1>
- 크레인 3대[6t, 8t, 9t]
- 박스 5개[2t, 5t, 2t, 4t, 7t]

i) 가벼운 크레인에 가벼운 박스부터
크레인1[6t] - [2t], [5t]
크레인2[8t] - [2t], [7t]
크레인3[9t] - [4t]
제일 긴 리스트의 길이 = 2 => 2분

ii) 무거운 크레인에 무거운 박스부터
크레인3[9t] - [7t], [2t]
크레인2[8t] - [5t], [2t]
크레인1[6t] - [4t]
제일 긴 리스트의 길이 = 2 => 2분

가벼운 크레인에 가벼운 박스부터 담기 == 무거운 크레인에 무거운 박스부터 담기
=> 단순 오름차순 정렬이냐, 내림차순 정렬이냐의 차이일 뿐
==============

<예제 입력 2>
- 크레인 2대[19t, 20t]
- 박스 7개[14t, 12t, 16t, 19t, 16t, 1t, 5t]

i) 가벼운 크레인에 가벼운 박스부터
크레인1[19t] - [1t], [12t], [16t], [19t]
크레인2[20t] - [5t], [14t], [16t]
제일 긴 리스트의 길이 = 4 => 4분

ii) 무거운 크레인에 무거운 박스부터
크레인2[20t] - [19t], [16t], [12t], [1t]
크레인1[19t] - [16t], [14t], [5t]
==============
'''
# ver1) 가벼운 크레인에 가벼운 박스부터 넣어보기 => 시간초과
'''
<풀이 방향>
- 가벼운 크레인(크레인을 오름차순 정렬)에 가벼운 박스(박스도 오름차순 정렬)부터 담아보자
'''
'''
# 1. 입력 받기
n = int(input())
crane_weight = sorted(list(map(int, input().split())))
m = int(input())
box_weight = sorted(list(map(int, input().split())))

# 2. 박스를 하나씩 크레인으로 이동
min = 0
while(box_weight): # O(M) = O(10,000)
    for crane in crane_weight: # O(N) = O(50), O(50 * 10,000) = O(500,000)
        for i in range(len(box_weight)): # O(M) = O(10,000), O(10,000 * 500,000) = O(5,000,000,000) = 50초 => 시간초과
            if crane < box_weight[i]: # 크레인에 담을 수 없는 상자는 패스
                continue
            else:
                del box_weight[i] # 크레인으로 배에 실어버림(리스트에서 제거)
                break # 다음 크레인으로 이동

    min += 1 # 모든 크레인으로 박스를 이동시키고 나면 1분 증가

# 3. 걸린 시간 출력
print(min)
'''

# ver2) 수학적 특징을 찾아서 적용해보기 => 틀렸습니다
'''
<풀이 방향>
예제 입력 4같은 경우에는 크레인이 [11, 17, 5, 2, 20, 7, 5, 5, 20, 7]으로 10개지만
가장 가벼운 박스의 무게가 15이므로 이보다 작은 크레인인 [11, 5, 2, 7, 5, 5, 7]의 7개는 필요가 없다.
따라서 사용가능한 크레인은 [17, 20, 20]의 3개뿐이다.

3개의 크레인을 사용하여 총 5개의 박스를 옮기는 데에 걸리는 시간은?
=> 2분(5//3 + 1) => 박스 개수 // 크레인 개수 + 1

=======
<반례>
3
10 10 10
6
1 1 1 1 1 1

이 경우 최소 시간은 2분이지만 위 코드 기준으로는 마지막에 1을 더해버려서 3분이 됨.
'''
'''
# 1. 입력 받기
n = int(input())
crane_weight = sorted(list(map(int, input().split())))
m = int(input())
box_weight = sorted(list(map(int, input().split())))

# 2. 최소 박스 무게보다 무게 제한이 낮은 크레인 찾기
for i in range(len(crane_weight)):
    if crane_weight[i] >= box_weight[0]: # 크레인이 박스의 최소 무게보다 더 들 수 있다면
        print( (len(box_weight)) // (len(crane_weight) - i) + 1 ) # box개수 // crane개수 + 1 
        break
'''


# ver3) ver1 코드 수정 => 시간 초과
'''
<풀이 방향>
- 크레인과 상자를 내림차순으로 정렬함
- 제한 하중이 큰 크레인으로 무거운 상자부터 옮기는 방식 사용
- 단, 반복을 하기 전 제일 무거운 상자를 옮길 수 있는 크레인이 없다면 -1을 출력 후 종료
- 
'''
'''
# 1. 입력 받기
n = int(input())
crane_weight = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
box_weight = sorted(list(map(int, input().split())), reverse=True)

# 만약! 어떠한 크레인으로도 박스를 옮길 수 없다면 -1 출력!
if crane_weight[0] < box_weight[0]:
    print(-1)
    exit()

# 2. 박스를 하나씩 크레인으로 이동(무거운 크레인에 무거운 박스부터)
min = 1 # 크레인, 박스는 모두 1개 이상이므로 최소 시간은 1분임
crane_index = 0
while box_weight: # O(10,000)
    # 현재 크레인이 가장 가벼운 박스조차 들 수 없다면 맨 앞 크레인으로 이동
    if crane_weight[crane_index] < box_weight[-1]:
        crane_index = 0
        min += 1
        continue

    # 크레인이 나를 수 있는 박스를 탐색
    box_index = 0
    while crane_weight[crane_index] < box_weight[box_index]:
        box_index += 1

    # 박스를 나르고(=삭제하고) 다음 크레인으로 이동
    del box_weight[box_index]
    crane_index += 1
    
    # 이때 다음 크레인이 처음 크레인이고, 아직 날러야 할 박스가 있다면
    # crane_index = 0, min += 1    
    if crane_index == n and box_weight:
        crane_index = 0
        min += 1

# 3. 걸린 시간 출력
print(min)
'''


# Final - Ver3 코드 정리
'''
<핵심포인트>
1. 불가능한 경우인지 체크
크레인이 [10, 9, 8]이고 박스가 [1000, 10, 1]이라고 가정해보자. 처음에는
'가장 무거운 박스를 나를 수 있는 크레인이 가장 가벼운 박스를 나를 수 있다면
불가능한 경우가 아니다'라고 생각했었다. 이 경우 10은 1을 나를 수 있으므로
불가능한 경우라고 판단되지 않는다.
그러나 가장 무거운 박스인 1000을 나를 수 있는 크레인이 없기 때문에 위 케이스는
불가능한 경우다. 따라서 관계식을 아래와 같이 세워야 한다.
  [가장 무거운 무게를 나를 수 있는 크레인] < [가장 무거운 박스] => 불가능!

2. 현재 크레인으로 남은 박스를 하나도 못옮기는 경우를 체크해야 함!!!
크레인이 [10, 5, 1]이라고 하고 남아있는 박스는 [6, 6, 6]이라고 가정해보자.
남아있는 박스를 옮길 수 있는 크레인은 크레인 10밖에 없다. 그러나 만약 크레인 5와
크레인 1인 경우에도 옮길 수 있는 상자가 있는지 확인하는 반복문을 돌리게 되면 이는
불필요한 실행이고, 시간초과가 뜨게 된다. 이 부분은 빠져서는 안되는 부분이다.
'''
# 1. 입력 받기
n = int(input())
crane_weight = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
box_weight = sorted(list(map(int, input().split())), reverse=True)

# 만약! 어떠한 크레인으로도 박스를 옮길 수 없다면 -1 출력!🔴
if crane_weight[0] < box_weight[0]:
    print(-1)
    exit()

# 2. 무거운 박스부터 이동
min = 0
while box_weight:
    for i in range(len(crane_weight)):
        # 현재 크레인으로 아무런 박스도 옮길 수 없는 경우, 첫 크레인으로 돌아감 🔴여기가 핵심!
        if box_weight and crane_weight[i] < box_weight[-1]:
            break

        for j in range(len(box_weight)):
            if crane_weight[i] >= box_weight[j]:
                del box_weight[j]
                break
    min += 1

# 3. 출력
print(min)