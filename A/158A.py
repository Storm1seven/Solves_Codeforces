n, k int(input())
a = list(map(int, input().split()))
x = 0
for i in range(n):
	if (a[i]>=a[k-1]):
		x+=1
print(x)