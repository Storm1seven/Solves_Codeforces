#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 12:36:29 2018

@author: subhash
"""
n, m = map(int, input().split())
a = []
flag = False
z = 0
for i in range(n):
	a.append(int(input(), 2))
for i in a:

		flag = True
		break
if flag:
	print('YES')
else:
	print('NO')