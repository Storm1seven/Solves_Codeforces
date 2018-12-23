def f(n):
	if n <= 0:
		return 0
	elif n == x[0] or n == x[1] or n == x[2]:
		return 1
	else:
		return max(f(n-x[0]), f(n - x[1]), f(n - x[2])) + 1
x = list(map(int, input().split()))
n = x[0]
x = x[1:]
if n%min(x) == 0:
	print(n//min(x))
else:	
	print(max(f(n-x[0]), f(n - x[1]), f(n - x[2])) + 1)