# edges = [[2, 3], [4, 3], [1, 1], [2, 1]]

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

# 86.5점 코드
# def solution(edges):
#     answer = [0, 0, 0, 0]

#     cnt = [[0, 0] for _ in range(len(edges) + 1)]

#     for edge in edges:
#         a = edge[0]
#         b = edge[1]
#         cnt[a][0] += 1
#         cnt[b][1] += 1

#     for i in range(1, len(cnt)):
#         c = cnt[i]

#         if c[0] >= 2 and c[1] == 0:
#             answer[0] = i
#         elif c[0] == 0 and c[1] > 0:
#             answer[2] += 1
#         elif c[0] >= 2 and c[1] >= 2:
#             answer[3] += 1

#     answer[1] = cnt[answer[0]][0] - answer[2] - answer[3]
#     print(answer)
#     return answer


def solution(edges):
    answer = [0, 0, 0, 0]

    cnt = dict({})
    
    for edge in edges:
        a = edge[0]
        b = edge[1]
        if not cnt.get(a):
            cnt[a] = [0, 0]
        if not cnt.get(b):
            cnt[b] = [0, 0]
        cnt[a][0] += 1
        cnt[b][1] += 1

    for i, c in cnt.items():
        # 나가는 간선 2개 이상, 들어오는 간선 0개: 생성한 쟁점
        if c[0] >= 2 and c[1] == 0:
            answer[0] = i
        # 나가는 간선 0개, 들어오는 간선 1개: 막대 그래프
        elif c[0] == 0 and c[1] > 0:
            answer[2] += 1
        # 들어오는 간선 2개 이상, 나가는 간선 2개 이상: 8자 모양
        elif c[0] >= 2 and c[1] >= 2:
            answer[3] += 1

    answer[1] = cnt[answer[0]][0] - answer[2] - answer[3]
    print(answer)
    return answer

solution(edges)