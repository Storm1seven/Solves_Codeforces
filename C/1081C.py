import operator as op
from functools import reduce
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom
n, m, k = map(int, input().split())
mod = 998244353
f = ncr(n-1, k)
f*=m
f*=(m-1)**k
f%=mod
print(int(f))