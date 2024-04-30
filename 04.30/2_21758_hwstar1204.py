# 꿀 따기 21758
"""
꿀통의 후보는 가장 큰값들 중 하나  (x)
꿀통의 후보는 오른쪽이나 왼쪽 끝 (x)
자기 자신빼고의 합이 가장 큰 수 두개가 꿀벌 위치 (x)
자기 자신빼고의 합이 가장 작은 수가 꿀통 위치  (x)

(왼쪽, 오른쪽)

idea : 상황을 나누어서 생각하기 
"""
# ver 1 24
# import sys 
# input = sys.stdin.readline
# n = int(input())  # 장소 개수
# h_list = list(map(int,input().split()))  # 꿀을 딸수 있는 양 리스트
# st = [[0,0] for _ in range(n)]   

# for i in range(n):
#     st[i][0] = sum(h_list[0:i])  # 왼쪽 합계   (자기자신 제외)
#     st[i][1] = sum(h_list[i+1:]) # 오른쪽 합계  (자기자신 제외)

# # for s in st:
#     # print(s)

# max_h = 0
# for i in range(n):
#     for j in range(i+1,n):

#         right1 = st[i][1] - h_list[j]
#         right2 = st[j][1]

#         left1 = st[i][0] 
#         left2 = st[j][0] - h_list[i]

#         # h_list_mid = max(h_list[i:j])
#         # idx = h_list.index(h_list_mid)
#         mid = right1-right2 + max(h_list[i:j])  # 사잇값의 합 + 가장 큰수(꿀통위치)


#         # 꿀통 위치에 따라 방향설정 (오른쪽, 왼쪽, 중앙)
#         max_h = max(max_h, right1+right2, left1+left2, mid) 

# print(max_h)


#left1 right1 ---- left2 right2 


# # ver2  55
# import sys
# input = sys.stdin.readline
# n = int(input())  # 장소 개수
# h_list = list(map(int,input().split()))  # 꿀을 딸수 있는 양 리스트
# st = [[0,0] for _ in range(n)]   

# for i in range(n):
#     st[i][0] = sum(h_list[0:i])  # 왼쪽 합계   (자기자신 제외)
#     st[i][1] = sum(h_list[i+1:]) # 오른쪽 합계  (자기자신 제외)

# # # for s in st:  # 각 장소기준 왼쪽 오른쪽 합을 저장한 리스트 출력 
# #     # print(s)

# max_h = 0

# for i in range(1, n-1):
#     right = (st[0][1] - h_list[i]) + st[i][1]  # 첫번째 벌 처음 위치 고정 (움직이는 벌위치 뺴주기)
#     max_h = right if max_h < right else max_h

# for i in range(1, n-1):
#     left = (st[-1][0] - h_list[i]) + st[i][0]  # 첫번째 벌 맨뒤 위치 고정 (움직이는 벌위치 뺴주기)
#     max_h = left if max_h < left else max_h

# for i in range(1,n-1):
#     mid = st[i][0] + st[i][1] - (h_list[0]+h_list[-1]) + 2*h_list[i]  # 장소기준 왼쪽합+오른쪽합 - 가장자리 벌 위치 + 2*꿀통
#     max_h = mid if max_h < mid else max_h


# print(max_h)



# ver 3  100
import sys
input = sys.stdin.readline
n = int(input())  # 장소 개수
h_list = list(map(int,input().split()))  # 꿀을 딸수 있는 양 리스트
st = [[0,0] for _ in range(n)]   

# 최적화~
st[0][0], st[0][1] = 0, sum(h_list[0+1:])  
for i in range(1,n):
    st[i][0] = st[i-1][0] + h_list[i-1]  # 왼쪽 합계   (자기자신 제외)
    st[i][1] = st[i-1][1] - h_list[i] # 오른쪽 합계  (자기자신 제외)

# for s in st:  # 각 장소기준 왼쪽 오른쪽 합을 저장한 리스트 출력 
#     print(s)

max_h = 0

for i in range(1, n-1):
    right = (st[0][1] - h_list[i]) + st[i][1]  # 첫번째 벌 처음 위치 고정 (움직이는 벌위치 뺴주기)
    max_h = max(max_h,right)

for i in range(1, n-1):
    left = (st[-1][0] - h_list[i]) + st[i][0]  # 첫번째 벌 맨뒤 위치 고정 (움직이는 벌위치 뺴주기)
    max_h = max(max_h,left)

for i in range(1,n-1):
    mid = st[i][0] + st[i][1] - (h_list[0]+h_list[-1]) + 2*h_list[i]  # 장소기준 왼쪽합+오른쪽합 - 가장자리 벌 위치 + 2*꿀통
    max_h = max(max_h,mid)


print(max_h)