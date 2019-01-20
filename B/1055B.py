from sys import stdin, stdout
input = stdin.readline
print = stdout.write
n, m, l = map(int, input().split())
a = list(map(int, input().split()))
count = 0
if a[0] > l:
	a[0] = 0
for i in range(1, n):
	if a[i] > l:
		a[i] = 0
	if a[i] == 0 and a[i-1] > 0:
		count+=1
for _ in range(m):
	z = list(map(int, input().split()))
	if len(z) == 1:
		print(str(count)+'\n')
	else:
		if a[z[1]-1]  == 0:
			pass
		elif a[z[1]-1]+a[z[2]] > l:
			a[z[1]-1] = 0
			if z[1] == 1:
				if a[1] != 0:
					count+=1
			elif z[1] == n:
				if a[-2]!=0:
					count+=1
			else:
				if a[z[1]-1]!=0 and a[z[1]]!=0:
					count+=1
		else:
			a[z[1]-1]+=a[z[2]]