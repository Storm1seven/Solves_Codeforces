n = int(input())
a = list(map(int, input().split()))
a.sort()
if n == 2:
	print(0)
else:
	print(min(a[-1] - a[1], a[-2] - a[0]))