'''
<문제>
[2024 KAKAO WINTER INTERNSHIP] - 가장 많이 받은 선물
https://school.programmers.co.kr/learn/courses/30/lessons/258712?language=python3

<입력>
- friends(2 <= friends <= 50) : 선물을 주고 받은 친구들의 수
- gifts(1 <= gifts <= 10,000) : [A, B] 형태의 입력(A: 선물을 준 친구, B: 선물을 받은 친구)

<출력>
- 가장 많은 선물을 받는 친구가 받을 선물의 수
'''
#  #  #  #  #  #
'''
<풀이 방향>
- 각각의 친구끼리 서로 주고 받은 선물의 관계를 기록해야 함 => 2차원 리스트 사용
- '선물 지수' = '준 선물' - '받은 선물' = '리스트 행의 합' - '리스트 열의 합'
'''


def solution(friends, gifts):
    # 친구 이름에 대한 인덱스를 저장
    friends_dict = dict()
    for i in range(len(friends)):
        friends_dict[friends[i]] = i

    # 선물 기록 저장할 2차원 리스트 선언
    gift_history = [ [0]*len(friends) for _ in range(len(friends)) ]
    
    # 생성한 리스트에 값 추가
    for gift in gifts:
        gift = gift.split()
        i = friends_dict[gift[0]]
        j = friends_dict[gift[1]]
        gift_history[i][j] += 1

    # 선물 지수 저장할 리스트 선언
    gift_value = []
    for i in range(len(friends)):
        gift_value.append(sum(gift_history[i]) - sum([ gift_history[k][i] for k in range(len(friends)) ]))

    # 친구 별 주고 받은 선물 비교하여 최종 결과 도출
    gift_count = [0] * len(friends) # 각각 받을 선물의 개수를 저장할 리스트
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if gift_history[i][j] > gift_history[j][i]:
                gift_count[i] += 1
            elif gift_history[i][j] < gift_history[j][i]:
                gift_count[j] += 1
            else: # 선물을 주고받은 갯수가 동일한 경우 -> '선물 지수' 비교
                if gift_value[i] > gift_value[j]:
                    gift_count[i] += 1
                elif gift_value[i] < gift_value[j]:
                    gift_count[j] += 1
                else: # '선물 지수'마저 동일한 경우 -> 생략
                    continue # 이 부분은 굳이 작성하지 않아도 되긴 하지만 구색을 갖추기 위해 작성

    return max(gift_count)


a = ["muzi", "ryan", "frodo", "neo"]
b = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

c = ["joy", "brad", "alessandro", "conan", "david"]
d = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

e = ["a", "b", "c"]
f = ["a b", "b a", "c a", "a c", "a c", "c a"]

print(solution(a, b))