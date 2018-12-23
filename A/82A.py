import math
a = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
n = int(input())
if n < 6:
	print(a[n-1])
else:
	t = math.ceil((math.log2(n//5)))-1
	rem = n - 5*2**t
	count = 2**t
	x = rem/count
	print(a[math.ceil(x)-1])