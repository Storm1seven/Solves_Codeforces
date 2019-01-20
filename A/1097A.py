c = input()
a = list(input().split())
flag = False
for i in a:
	if c[0] in i or c[1] in i:
		print('YES')
		flag = True
		break
if not flag:
	print('NO')