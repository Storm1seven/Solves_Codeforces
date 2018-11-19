t = int(input())
for _ in range(t):
	i = input()
	if len(i) > 4:
		print(i[1]+str(len(i)-2)+i[-1])
	else:
		print(i)