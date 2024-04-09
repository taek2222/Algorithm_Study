#오리 
"""
오리의 울음소리 : 'quack' 한번 또는 그 이상 
조건
1. 울음소리가 연속적이지 않아도 됨
2. 울음소리 순서 지켜져야함 

입력: 5 <= 소리 길이 <= 2500, q,u,a,c,k로만 이루어짐 
출력: 오리의 최소 수 구하기 단, 녹음한 울음 소리가 올바르지 않으면 -1 (울음소리가 0개일떄)

testcase
quqacukqauackck
quack quack
quack




qua ck?? 남은 소리 2개임
ack 버려지는 소리 (각 문자 앞에 있어야할 문자가 없어서 넘김)
# 완성된 소리 이후 q가 나오면 연속된 울음 == k 다음에 q가 나오는 개수가 연속된 울음이므로 전체에서 연속된 울음수 빼야함 
-> 그냥 k 다음에는 q가 오도록 설정 ( 선택된 소리가 q이면 맨뒤 소리가 k인게 없으면 새로 생성 )

오리 3
연속 울음 수 1
# quack
# quack
# quack

testcase 2
kcauq -> 오리수 0 -> -1

testcase 3
quack quack quack quack quack quack quack quack quack quack


testcase 5
qu qa qu ua ca kc qc kk ua qu ck qa uc ka ck
quackquackquack
quackquack
quack

testcase 6
quackqauckquack
quackq
a?
-1인 경우는 소리중 앞에 와야하는 소리가 리스트 안에 단어들 중 없을때 -1 break


idea
각 단어를 돌면서
정답 후보 리스트를 돌면서 후보 단어의 마지막부분 검사하면서 

    그 단어 앞에 있어야만 하는 단어가 없으면 break print(-1)
    그 단어 앞에 있어야만 하는 단어가 있으면 그 단어 뒤에 추가
        q: 단어뒤에 k있는 단어, 없으면 그냥 새로 리스트에 추가 
        u: 단어뒤에 q있는 단어
        a: 단어뒤에 u있는 단어
        c: 단어뒤에 a있는 단어
        k: 단어뒤에 c있는 단어 

    오리수 = len(리스트)

"""
import sys
input = sys.stdin.readline
sounds = list(input().rstrip())
ori = []

if sounds[0] != "q"  or  sounds[-1] != "k" or len(sounds) % 5 :
    print(-1)
    exit()

for s in sounds:
    if s == 'q':
        ori.append(s)                       # 일단 q 추가 

    for i,o in enumerate(ori):
        end_word = o[-1]                    # 저장된 소리의 마지막 소리 단어

        if s == 'q':
            if end_word == 'k':
                ori[i] = s
                ori.pop()                   # 추가했던 q 삭제
            elif i != (len(ori)-1):
                continue
            break
        
        elif end_word == 'q' and s == 'u':
            ori[i] = s                      # 해당 소리 단어 뒤에 추가 
            break
        elif end_word == 'u' and s == 'a':
            ori[i] = s
            break
        elif end_word == 'a' and s == 'c':
            ori[i] = s
            break
        elif end_word == 'c' and s == 'k':       
            ori[i] = s
            break

    else:                                    # 앞에 있어야할 단어가 없는 경우                    
        print(-1)
        exit()                               # 프로그램 종료

print(len(ori))