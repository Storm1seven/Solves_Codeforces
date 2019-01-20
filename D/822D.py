#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 22:25:54 2018

@author: subhash
"""

def smallest_fac(n):
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			return i
	return n
def f(n):
	i = 0
	sf = smallest_fac(n)
	if smallest_fac(n) == n:
		return n*(n-1)//2
	else:
		if dp[n//sf]:
			i+=n//sf * dp[sf] + dp[n//sf]
		else:
			i+=n//sf * dp[sf] + f(n//sf)
	return i
t, l, r = map(int, input().split())
dp = [0]*(r+1)
dp[2] = 1
dp[3] = 3
answer = 0
for i in range(4, len(dp)):
	dp[i] = f(i)
for i in range(r-l + 1):
	answer+=t**i * dp[l+i]
	answer%=10**9 + 7
f = open("demofile.txt", "a")
f.write(str(dp))
print(answer)