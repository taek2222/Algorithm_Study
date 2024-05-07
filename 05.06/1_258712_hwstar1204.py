# 가장 많이 받은 선물 
"""
친구들끼리 선물 주고받은 기록을 가지고 다음날 누가 선물을 많이 받을지 예측 

    1. 두사람 사이에 선물 더 많이 준 사람 :  상대한테 하나 받음 
    2. 주고받은 기록이 없음 OR 주고받은 수가 같음 : 선물지수가 더 큰사람이 받음 

    선물 지수 = 친구들에게 준 선물 수 - 받은 선물수

Idea
주고받은 선물 =  2차원 리스트
선물 지수 = 1차원 리스트 

주고받은 선물 리스트에서 1번째 사람부터 대각선으로 비교 계산 
max = 0 초기화 후 한사람 반복 끝나면 max와 비교 계산 후 대입 

"""
friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]

nums = len(friends)  # 친구 수
name_dict = {}  # 이름 -> 숫자로 변환
for i, name in enumerate(friends):
    name_dict[name] = i
    
board = [[0] * nums for _ in range(nums)]  # 주고받은 선물 개수 
for g in gifts:
    a,b = g.split()
    an, bn = name_dict[a], name_dict[b]
    board[an][bn] += 1

values = [0] * nums  # 선물 지수 
for i in range(nums):
    give = sum(board[i])
    receive = sum( b[i] for b in board )
    values[i] = give - receive

predict = [0] * nums  # 친구들이 이번달 받을 선물개수
for i in range(nums):
    for j in range(nums):
        if i == j:  # 자신끼리 비교 X
            continue

        sender, receiver = board[i][j], board[j][i] # 

        if sender > receiver:
            predict[i] += 1
        elif sender == receiver:
            if values[i] > values[j]: # 선물지수가 상대보다 높을때
                predict[i] += 1
        elif sender < receiver:
            continue

        # max와 지금부터 아직 검사안한 친구로부터 모두 선물 받을 수 비교
        # -> max가 더 크면 내부 반복문 종료 (검사할필요없음)

print(max(predict))