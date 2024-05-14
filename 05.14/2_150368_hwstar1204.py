"""
목표
    1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
    2. 이모티콘 판매액을 최대한 늘리는 것.
입력
    users : 사용자의 구매 기준을 담은 2차원 배열
        [비율, 가격], 1 <= users <= 100
    emoticons : 이모티콘들의 정가를 담은 1차원 배열
        1 <= emoticons <= 7

    조건
        할인 종류 : 10%, 20%, 30%, 40%
        1 <= 비율 <= 40
        100 <= 사용자의 가격 <= 1,000,000
        100 <= 이모티콘 가격 <= 1,000,000

출력
    목표를 최대로 달성했을때 [이모티콘 플러스 가입 수, 이모티콘 매출액]

Idea - 완전 탐색

"""
# users = [[40, 10000], [25, 10000]]
# emoticons = [7000, 9000]

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]

# rates = [10,20,30,40]
rates = [40,30,20,10]
result = []

for q in rates:
    for w in rates:
        for e in rates:
            for r in rates:  # 모든 비율의 경우의 수

                total_join, total_price = 0,0  # 각 비율에 해당하는 모든 유저의 가입수, 구매 가격

                for user in users:
                    user_rate, user_price = user
                    joined, tmp_price = False,0

                    for rate, emoticon_price in zip([q,w,e,r],emoticons):  # 이모티콘 할인 비율에 대한 계산
                        
                        # 이모티콘 사는 경우
                        if user_rate <= rate:  
                            tmp_price += (emoticon_price // 100 * (100 - rate))  # 미리 저장해서 최적화 가능

                        # 서비스 가입하는 경우
                        if user_price <= tmp_price:  
                            joined = True
                            break  # 서비스 가입하면 다음 이모티콘 가격 계산할 필요없음
                    
                    if joined:
                        total_join += 1
                    else:
                        total_price += tmp_price
 

                result.append([total_join,total_price])  # 정답 후보군 추가 (끝까지 다 해본 후 비교해야함)

answer = sorted(result, key=lambda x : (x[0],x[1]))  # 가입수, 가격 순으로 정렬
                
print(answer[-1])  # 가장 많은 가입수이면서 가장 큰 가격을 가진 경우






# if total_join >= answer[0]:
#     if total_price > answer[1]:
#         answer[0] = total_join
#         answer[1] = total_price