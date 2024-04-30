'''
https://www.acmicpc.net/problem/17413
<문제>
- 입력받은 문자열의 각 단어별 순서를 뒤집어서 출력하는 문제
- 문자열은 소문자 알파벳, 숫자, 공백, '<', '>'로만 이루어져 있음
- '<'와 '>'안에 있는 문자열(태그)은 뒤집지 않고 그대로 출력
- 태그 내에 있는 공백 역시 뒤집지 않음
- 열린 태그는 반드시 닫힘
- 태그 내의 태그는 없는듯
- 태그와 단어 사이에는 공백이 없다

<입력>
- 문자열 S(1 <= S <= 100,000)

<출력>
- 뒤집은 문자열
'''

# 1. 입력
s = input()
res = ''
start = 0
Tag = False

# 2. s를 반복<
for i in range(len(s)):
    if s[i] == '<': # 열린 태그라면 start 인덱스 설정하고 Tag라는 표시를 함
        if i != 0:
            res += s[start:i][::-1] # 만약 앞이 단어였다면 추가
        start = i
        Tag = True
        continue
    elif s[i] == '>': # 닫힌 태그라면 Tag문자열 추가하고 start 인덱스 재설정 및 Tag 아님 표시
        res += s[start:i+1]
        start = i+1
        Tag = False
        continue
    elif s[i] == ' ' and Tag == False: # 공백이고 태그가 아닌 경우
        res += s[start:i][::-1] + ' '
        start = i+1
        continue
    elif i == len(s)-1: # 태그가 아니고 마지막 문자라면 지금까지의 문자열 출력
        res += s[start:i+1][::-1]

# 3. 출력
print(res)