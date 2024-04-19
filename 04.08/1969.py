'''
<조건>
1 <= N <= 1000
1 <= M <= 50

<출력>
DNA의 종류 4개를 조합하여 입력받을 dna의 행을 기준으로 Hamming Distance의 합이 최소가 되는 조합을 출력.
Hamming Distance의 합이 가장 작으려면 4개 중에서 i번째 행에 제일 많이 있는 문자(dna)를 고르면 됨.

<핵심>
입력받은 문자열을 행을 기준으로 실행해야 함.
이를 위해 입력받는 순간에 행을 기준으로 저장되도록 변경.
'''

N, M = map(int, input().split())
input_dna = [""] * M
DNA = ['A','C','G','T']
for _ in range(N): # O(N), 최대: O(1,000)
    s = input()
    
    # 문자열을 미리 같은 행끼리 문자열을 이룰 수 있도록 저장
    for i in range(M): # O(N*M), 최대: O(1,000 * 50) = O(50,000)
        input_dna[i] += s[i]

sum_distance = 0
result = ""
for i in input_dna:
    max = 0
    ch = ''
    for c in DNA:
        if max < i.count(c):
            max = i.count(c)
            ch = c
    result += ch
    sum_distance += N - max
    
print(result)
print(sum_distance)