import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())
def lcm(a, b):
    return (a*b)//math.gcd(a, b)
a, b = sorted(listin())
x, y = a, b
l = lcm(a, b)
k = l - b
ans = 0
while k:
    k//=2
    templ = lcm(x+k, y+k)
    if templ < l:
        l = templ
        x+=k
        y+=k
        ans = x - a
print(ans)
