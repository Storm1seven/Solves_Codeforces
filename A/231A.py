n = int(input())
a = []
for i in range(n):
	b = list(map(int, input().split()))
	a.append(b)
x = 0
for i in range(n):
	p = 0
	for j in range(3):
		if a[i][j]==0:
			p+=1
	if p==1 or p==0:
		x+=1
print(x)