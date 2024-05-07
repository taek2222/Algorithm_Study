# friends = ["muzi", "ryan", "frodo", "neo"]
# gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

# friends = ["joy", "brad", "alessandro", "conan", "david"]
# gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]

def solution(friends, gifts):
    answer = [0 for _ in friends]
    gift_dic = {}
    gift_idx = {}
    
    for friend in friends:
        gift_dic[friend] = {}
        gift_idx[friend] = 0
    
    for gift in gifts:
        t, f = gift.split()
        if f in gift_dic[t]:
            gift_dic[t][f] += 1
        else:
            gift_dic[t][f] = 1
        gift_idx[t] += 1
        gift_idx[f] -= 1
    
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if friends[j] in gift_dic[friends[i]]:
                a = gift_dic[friends[i]][friends[j]]
            else:
                a = 0
            if friends[i] in gift_dic[friends[j]]:
                b = gift_dic[friends[j]][friends[i]]
            else:
                b = 0
            
            if a > b:
                answer[i] += 1
            elif a < b:
                answer[j] += 1
            else:
                x, y = gift_idx[friends[i]], gift_idx[friends[j]]
                if x > y:
                    answer[i] += 1
                # else:
                #     answer[j] += 1
                elif x < y:
                    answer[j] += 1
    print(max(answer))
    return max(answer)
    

solution(friends, gifts)