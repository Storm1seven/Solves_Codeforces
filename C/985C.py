#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 13:44:52 2018

@author: subhash
"""

n, k, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
max_vol = a[0]
limit = n+1
for i in range(n*k):
	if a[i] - a[0] > l:
		limit = i - 1
		break
if limit+1 < n:
	print('0')
else:
	rem = (n*k - limit)//k
	max_vol+=sum(a[limit - rem:limit+1])
	rem1 = n - 1 - rem
	max_vol+=sum(a[1:rem1])
	print(max_vol)