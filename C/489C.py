m, s = map(int, input().split())
if s > m*9:
	print(-1, -1)
elif s == m*9:
	print('9'*m, '9'*m)
else:
	x = s//9
	