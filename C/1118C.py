import collections
n = int(input())
a = list(map(int, input().split()))
z = collections.Counter(a)
flag = 0
for i in z.values():
    if i%4:
        flag+=1
if n%2 == 0 and flag:
    print('NO')
elif n%2 == 1 and flag != 1:
    print('NO')
else:
    print('YES')
    matrix = [[0]*n]*n
    for i in matrix:
        print(*i)