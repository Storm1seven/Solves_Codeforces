n, m = map(int, input().split())
a = []
for _ in range(n):
	a.append(list(input().split()))
for i in range(n):
	if "".join(a[i])=='.'*m :
		a.remove(a[i])
	for j in range(n):
		count = 0
		if a[j][i] == '*':
			break
		else:
			count+=1
		if count == n:
			

	
