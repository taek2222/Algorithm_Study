'''
<조건>
오리의 울음소리는 q, u, a, c, k 순서여야만 함
울음소리 문자열의 길이는 5이상 2500이하임

<문제 해설>
qu_ac_kq_uack__
__q__u__a____ck

quack 문자열이 완성되기 전에 다른 quack 문자열의 일부가 포함되어 있다면
이는 두마리의 오리가 있는 것.

quack 문자열이 완성되고 다시 quack 문자열이 나오는 순서라면 이는 한마리의
오리가 계속해서 울고있는 것.

<예제>
quqaquuacakcqckkuaquckqauckack
qu_a____c_k_q___ua__ck________
__q__u_a___c__k___qu___a_ck___
____q_u__a___c_k______q_u__ack

=> 한 오리가 울고 있을 때 울기 시작하는 다른 오리가 있는지 없는지 확인
=> quack가 완성되는 범위 내에 존재하는 q의 최대 개수가 오리의 마릿수
=> 단, quack 순서에 어긋나거나 quack 문자열 완성이 안되면 -1을 리턴

<입력>
오리의 울음소리

<출력>
오리의 마릿수
'''
# 1. 입력 받기, 오리 울음소리 리스트(DUCK), 등장 횟수 카운트 리스트(count) etc
sound = input()
DUCK = {
    'q': 0,
    'u': 1,
    'a': 2,
    'c': 3,
    'k': 4
}
count = [0] * 5
cross = False # 엇갈리지 않으면 False, 엇갈렸으면 True
max = 1 # 오리의 마릿수

# 2. 'quack'가 만들어지면(=> 'k'가 나오면) 그때의 'q'의 갯수가 오리의 최대 마릿수
for c in sound:
    if cross: # 엇갈렸다면 중지
        break

    pos = DUCK.get(c) # 등장한 문자의 인덱스를 pos에 저장
    if pos == 4:
        if max < count[0]: # 최대 마릿수보다 현재 마릿수가 더 크다면 최대 마릿수 수정
            max = count[0]

        for i in range(pos): # quack 문자열이 완성되었으니 전체 카운트 1씩 감소
            count[i] -= 1
    else:
        count[pos] += 1 # 등장한 문자의 카운트를 1 증가
    
    # 문자의 숫자가 엇갈렸다면 바로 -1을 리턴
    for i in range(pos):
        if count[pos] > count[i]: # 뒤에 나오는 문자의 횟수가 앞에 나온 문자의 횟수보다 많으면 엇갈린 것
            cross = True

# 4. 출력
print(-1 if cross or count.count(0) != 5 else max) # 엇갈리거나 남은 문자가 있으면 -1을, 아니라면 오리 마릿수를 출력