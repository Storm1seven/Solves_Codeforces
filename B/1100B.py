from sys import stdin, stdout
input = stdin.readline
print = stdout.write
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())
n, m = mapin()
a = listin()
d = {}
z = set(a)
s = set([])
for i in range(1, n+1):
    if i in z:
        continue
    else:
        print('0'*m + '\n')
        exit()
for i in a:
    d.setdefault(i, 0)
for i in a:
    d[i]+=1
    s.add(i)
    if len(s) == n:
        print('1')
        for j in d:
            d[j]-=1
            if d[j] == 0:
                s.remove(j)
    else:
        print('0')
print('\n')