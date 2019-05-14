import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())
n, q = mapin()
a = defaultdict(list)
for i in range(q):
    u, v = mapin()
    u, v = u-1, v-1
    for j in range(u, v+1):
        if len(a[j]) < 3:
            a[j].append(i)
total = len(a)
mark = []
for _ in range(q):
    mark.append([0]*q)
