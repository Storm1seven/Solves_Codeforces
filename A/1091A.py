def f(a, b, c):
	if a+1<=b and a+2<=c:
		return (3*a + 3)
	else:
		return f(a-1, b, c)
a, b, c = map(int, input().split())
print(f(a, b, c))
