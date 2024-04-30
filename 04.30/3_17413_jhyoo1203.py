data = input()

arr = []
res = ''
check = False
for d in data:
    if d == '<':
        check = True
        for _ in range(len(arr)):
            res += arr.pop()

    arr.append(d)
    if d == '>':
        check = False
        for _ in range(len(arr)):
            res += arr.pop(0)
    
    if d == ' ' and check == False:
        for i in range(len(arr)):
            if i == 0:
                arr.pop()
                continue
            res += arr.pop()
        res += ' '

if arr:
    for _ in range(len(arr)):
        res += arr.pop()

print(res)