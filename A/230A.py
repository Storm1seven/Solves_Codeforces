s, n = map(int, input().split())
d = {}
z = []
for _ in range(n):
	x, y = map(int, input().split())
	z.append(x)
	d[x] = y
z.sort()
flag = False
while z[0] < s:
	s+=d[z[0]]
	z.remove(z[0])
	if z == []:
		flag = True
		break
if flag:
	print('YES')
else:
	print('NO')