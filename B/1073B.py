n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = {}
for i in range(n):
	d[a[i]] = i
current = 0
for i in b:
	if d[i]+1 > current:
		print(d[i]+1-current, end = ' ')
		current = d[i]+1
	else:
		print(0, end = ' ')
print()
