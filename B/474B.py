def fit(n, z):
	while (low <= high):
		mid = (low+high)//2
		if z[mid] == n:
			return mid+1
		elif z[mid]< n < z[mid+1]:
			return mid +2
		elif z[mid-1]< n < z[mid]:
			return mid
		elif z[mid] < n:
			low = mid+1
			fit(n, z)
		else:
			high = mid-1
			fit(n, z)
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
z = []
for i in range(1, n+1):
	z.append(sum(a[:i]))
for i in b:
	print(fit(i, z))