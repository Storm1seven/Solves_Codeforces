m = 1000000007
n, q = map(int, input().split())
a = input()
t = []
count = 0
for i in a:
	if i == '1':
		count+=1
	t.append(count)
for _ in range(q):
	x,y=map(int,input().split())
	if(x==1):
		p=t[y-1]
	else:
		p=t[y-1]-t[x-2]
	q=(y-x+1-p)	
	s=pow(2,p+q,m) - (pow(2,q,m))	
	print(s%m)