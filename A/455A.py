n = int(input())
a = [0]*100001
b = list(map(int, input().split()))
for i in b:
	a[i]+=1
c = [0]*100001
for i in range(len(a)):
	c[i] = i*a[i]
for i in range(1, len(c)-1):
	if c[i-1] == 0 and c[i+1] == 0:
		ans+=c[i]
		c[i] == 0