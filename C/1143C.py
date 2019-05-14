import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())
n = int(input())
d = defaultdict(list)
for i in range(n):
    p, c = mapin()
    d[p].append((i+1, c))
ans = []
for i in range(1, n+1):
    flag = True
    for v, c in d[i]:
        if c == 0:
            flag = False
            break
    if flag:
        ans.append(i)
ans.sort()
print(*ans)
