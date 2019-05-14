import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())
n, m, k = mapin()
a = listin()
z = sorted(a)
d = defaultdict(int)
for i in range(1, k*m+1):
    d[z[-i]]+=1
s = 0
for i, j in d.items():
    s+=i*j
index = []
count = 0
for i in range(n):
    if a[i] in d:
        if d[a[i]]:
            d[i]-=1
            count+=1
    if count == m:
        index.append(i+1)
        count = 0
print(s)
print(*index)