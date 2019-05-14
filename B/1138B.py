import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())
n = int(input())
c = input()
a = input()
d = defaultdict(int)
for i in range(n):
    d[(c[i], a[i])]+=1
