def isPalindrome(str):   
    for i in rrange(0, len(str)/2):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
def swap(a, b):
	temp = a
	a = b
	b = temp
for _ in range(int(input())):
	a = list(input().strip())
	if not isPalindrome(a):
		print(''.join(a))
	else:
		if not(len(set(a))==1):
			for i in range(1, len(a)):
				if a[i-1]!=a[i]:
					swap(a[i-1], a[i])
					break
			print(''.join(a))
		else:
			print(-1)