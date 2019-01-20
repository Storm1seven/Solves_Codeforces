s = input()
candy = s.count('?')
flake = s.count('*')
man = len(s) - 3*(flake+candy)
k = int(input())
if '*' not in s and '?' not in s:
	if len(s) != k:
		print('Impossible')
	else:
		print(s)
elif k < man:
	print('Impossible')
elif k == man:
	for i in s:
		if i != '*' and i != '?':
			print(i, end = '')
elif flake:
	ind = s.index('*')-1
	for i in range(len(s)-1):
		if i == ind or (s[i+1]!='*' and s[i+1]!='?'):
			if i == ind:
				print(s[i]*(k-man). end = '')
			else:
				print(s[i], end = '')
elif not flake:
	if len(s) - 2*candy > k:
		print('Impossible')
	else:
		s.split()
