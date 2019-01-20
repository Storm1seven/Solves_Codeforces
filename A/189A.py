from collections import deque
def calc(n, a, b, c):
	k = []
	while z:
		first = z.popleft()
		operations = [a, b, c]
		for i in operations:
			if i >= n:
				operations.remove(i)
		if first[0] == n:
			k.append(first[1])
		else:
			for i in operations:
				if first[0] + i <= n:
					z.append((first[0]+i, first[1]+1))
	return max(k)	
n, a, b, c = map(int, input().split())
z = deque([(0, 0)])
print(calc(n, a, b, c))