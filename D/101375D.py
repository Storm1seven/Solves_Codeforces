n = int(input())
h = list(map(int, input().split()))
k = sum(h)**2
s = 0
for i in h:
	s+=i**2
print((k-s)//2) 