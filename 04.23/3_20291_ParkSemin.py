'''
<문제>
- 파일을 확장자 별로 정리하여 각각 이름과 갯수 출력
- 확장자 이름은 오름차순으로 정렬하여 출력

<입력>
- 첫째 줄: n(1 <= n <= 50,000) - 파일 개수
- N개 줄: 파일 명(abc.txt 등의 형태)

<출력>
- 총 확장자의 개수만큼(파일 개수가 아닌 확장자의 개수임) 출력
- "확장자명 개수"의 형태로 출력


'''

# ver1) 시간복잡도는 무시하고 극한의 숏코딩 => 시간 초과
'''
<풀이 방향>
1. 파일명에서 '.'뒤의 확장자 명만 있으면 되므로 '.' 뒤의 문자열만 입력받는다.
2. 집합 set을 사용하여 중복을 제거하고 오름차순으로 정렬한다.
3. extension.count('확장자명')을 사용하여 확장자별 개수를 출력한다.
'''
'''
# N의 최대값이 50,000이므로 readline 사용
import sys
input = sys.stdin.readline

# 1. 입력 받기
n = int(input())
extension = [input().rstrip().split('.')[1] for _ in range(n)]

# 2. 출력
for ex in sorted(set(extension)):
    print(ex, extension.count(ex))
    # N = 50,000이고 모든 확장자는 서로 다르다고 할 때
    for문과 count함수의 시간복잡도는 둘다 O(50,000)이므로
    전체 시간복잡도는 O(2,500,000,000) => 25초가 된다.
'''

# ver2) 시간복잡도 O(N)으로 단축 - 39044KB, 192ms
'''
<풀이 방향>
1. ver1과 입력은 동일하게 받지만 집합을 사용하지 않고 리스트를 정렬한다.
2. 정렬한 리스트를 for문으로 출력한다.
  - 동일한 확장자는 첫번째 것만 출력한다.
  - 다음 출력이 동일한 확장자라면 cnt를 1 증가한다.
  - 다음 출력이 다른 확장자라면 cnt를 출력하고 1로 초기화한다.
'''
'''
# N의 최대값이 50,000이므로 readline 사용
import sys
input = sys.stdin.readline

# 1. 입력 받기
n = int(input())
extension = sorted([input().rstrip().split('.')[1] for _ in range(n)])

# 2. O(N) for문
temp = ''
cnt = 0
for ex in extension:
    if temp != ex:
        if cnt:
            print(cnt)
        cnt = 1
        temp = ex
        print(temp, end=' ')
    else:
        cnt += 1
print(cnt) # 마지막 확장자에 대한 카운트 출력
'''

# ver3) 딕셔너리 사용 - 43604KB, 220ms
# 딕셔너리는 1차적으로 키를 정렬하고 정렬된 키 값을 기준으로 다시 원래의
# 딕셔너리에서 값을 찾기 때문에 리스트의 정렬보다 시간이 더 소요된다.
import sys
input = sys.stdin.readline

# 1. 입력 받기
n = int(input())
extension = dict()
for _ in range(n):
    ex = input().rstrip().split('.')[1]
    if extension.get(ex):
        extension[ex] += 1 # 있으면 개수 1 증가
    else:
        extension[ex] = 1 # 없으면 딕셔너리에 추가

# 2. 오름차순 정렬하여 출력
for item, value in sorted(extension.items()):
    print(item, value)