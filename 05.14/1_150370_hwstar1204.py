"""
입력
today : 오늘 날짜 ('YYYY.MM.DD')
terms : 약관의 유효기간을 담은 1차원 배열 (1<=len<=20)
privacies : 수집된 개인정보의 정보를 담은 1차원 배열 (1<=len<=100)

출력 : 파기해야할 개인정보 보호를 오름차순으로 1차원 정수 배열 
"""

# today = "2022.05.19"
# terms = ["A 6", "B 12", "C 3"]
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# result = [1, 3]

today = "2020.01.01"	
terms = ["Z 3", "D 5"]	
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]	
# result = [1, 4, 5]

answer = []
today = list(map(int,today.split('.'))) # 오늘 날짜 

t_dict = dict()
for t in terms:
    alphabet, mounth = t.split()
    t_dict[alphabet] = int(mounth)

for i, p in enumerate(privacies):
    tmp, palpha = p.split()
    py, pm, pd = map(int,tmp.split('.'))  # 2021 5 2 A

    if today[0] > py + (pm + t_dict[palpha]) // 12:  # 계산한 연도만 비교
        answer.append(i+1)
        continue

    y = (today[0] - py) * 336  # 12 * 28
    m = (today[1] - pm) * 28
    d = today[2] - pd

    # 오늘 기준으로 개인정보 수집된 일수 차이 비교
    if t_dict[palpha]*28 <= y+m+d:  # day로 환산했을때 
        answer.append(i+1)
        continue

print(answer)
