# DNA
"""
DNA의 종류는 4가지 : A,T,G,C
Hamming Distance: 같은 길이의 문자열에서 다른 글자 개수 
n개의 길이가 m인 DNA 중에 Hamming Distance의 합이 가장 작은 DNA 찾기 

제한시간 : 2 sec
입력 조건: 0 < n <= 1000, 0 < m <= 50 
** 출력 조건: 그러한 DNA가 여러 개 있을 때에는 사전순으로 가장 앞서는 것을 출력한다. **

idea
    1. 문자열들을 2차원 배열에 저장
    2. 0 ~ m 까지 세로로 비교하면서 딕셔너리에 해당 알파벳 개수를 저장
    3. 딕셔너리의 max값이면서 사전순으로 앞서는 것을 선택 
    4. n에서 가장 많이 선택된 알파벳 개수를 뺀값을 저장 
"""
# Ver 1
import sys
inut = sys.stdin.readline

n,m = map(int,input().split())
dna = [list(input()) for _ in range(n)]
cnt = 0
answer = ''

for i in range(m):
    dna_dict = {'A':0, 'T':0, 'G':0, 'C':0}
    for j in range(n):
        dna_dict[dna[j][i]] += 1
    
    max_cnt = 0  # 최댓값 저장
    m = ''       # 최댓값을 가지고 사전순으로 가장 앞서는 dna 저장
    for k in ['A', 'C', 'G', 'T']:  # 같은 개수의 dna가 있으면 사전순
        if dna_dict[k] > max_cnt:
            max_cnt = dna_dict[k]
            m = k

    # d = max(dna_dict,key=dna_dict.get) 사전순 정렬이 안되서 틀림
    cnt += n - max_cnt
    answer += m
print(answer)
print(cnt)





# Ver 2 defaultdict 라이브러리를 이용한 풀이 
import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
dna = [list(input().strip()) for _ in range(n)]
cnt = 0
answer = ''

for i in range(m):
    dna_dict = defaultdict(int)
    for j in range(n):
        dna_dict[dna[j][i]] += 1   # 딕셔너리에 해당 key가 없어도 key를 만들어서 저장 
    
    max_cnt = max(dna_dict.values())  # 최댓값 구하기
    max_chars = [char for char, count in dna_dict.items() if count == max_cnt]  # 최댓값을 가지는 문자들 모으기
    m = min(max_chars)  # 사전순으로 가장 앞서는 문자 선택 (같은 최대값을 가지는 dna 후보 중)
    
    cnt += n - max_cnt
    answer += m

print(answer)
print(cnt)
