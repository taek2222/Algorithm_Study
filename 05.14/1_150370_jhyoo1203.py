today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

# today = "2020.01.01"
# terms = ["Z 3", "D 5"]
# privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]


def solution(today, terms, privacies):
    answer = []
    terms_dic = {}
    
    y, m, d = map(int, today.split('.'))
    
    for term in terms:
        a, b = term.split()
        terms_dic[a] = int(b)
    
    for i, privacy in enumerate(privacies, start=1):
        deadline, term = privacy.split()
        d_y, d_m, d_d = map(int, deadline.split('.'))
        
        add_mon = terms_dic[term]
        
        d_m += add_mon
        while d_m > 12:
            d_m -= 12
            d_y += 1
        
        if (y, m, d) >= (d_y, d_m, d_d):
            answer.append(i)
    
    return answer



print(solution(today, terms, privacies))