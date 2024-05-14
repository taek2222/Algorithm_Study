# 모든 달은 28일까지 있다고 가정
# 파기해야 할 개인정보의 번호는 "오름차순"으로 정렬

def solution(today, terms, privacies):
    answer = []
    today_int = list(map(int, today.split('.'))) # 오늘 날짜를 정수 형식으로 변환
    
    # 1. 약관 종류 딕셔너리
    terms_dict = dict()
    for t in terms:
        i, j = t.split()
        terms_dict[i] = int(j)
        
    # 2. 파기할 개인정보 탐색
    for index in range(len(privacies)):
        i, j = privacies[index].split()
        term = terms_dict[j] # 약관 종류에 대한 기간
        date = list(map(int, i.split('.'))) # 개인정보가 수집된 날짜
        
        date[1] += term
        while date[1] > 12:
            date[0] += 1 # 연도 1 증가
            date[1] -= 12 # 12개월(1년) 뺄셈
            
        # 오늘 날짜와 비교
        if (today_int[0] > date[0]) or (today_int[0] == date[0] and today_int[1] > date[1]) or (today_int[0] == date[0] and today_int[1] == date[1] and today_int[2] >= date[2]):
            answer.append(index+1)
          
    return answer            