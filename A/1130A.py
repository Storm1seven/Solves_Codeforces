import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())
n = int(input())
z = listin()
numpos = 0
numneg = 0
for i in z:
    if i < 0:
        numneg +=1
    elif i > 0:
        numpos +=1
if numpos >= n//2 + int(n%2):
    print(1)
elif numneg >= n//2 + int(n%2):
    print(-1)
else:
    print(0)