def leastPrimeFactor(n): 
    least_prime = [0] * (n + 1)  
    least_prime[1] = 1
    for i in range(2, n + 1):
        if (least_prime[i] == 0):
            least_prime[i] = i 
            for j in range(2 * i, n + 1, i) : 
                if (least_prime[j] == 0) : 
                    least_prime[j] = i
    return least_prime
def f(n):
	i = 0
	sf = least_prime[n]
	if sf == n:
		return n*(n-1)//2
	else:
		if dp[n//sf]:
			i+=n//sf * dp[sf] + dp[n//sf]
		else: 
			i+=n//sf * dp[sf] + f(n//sf)
			dp[n//sf] = i
	return i
t, l, r = map(int, input().split())
dp = [0]*(r+1)
dp[2] = 1
dp[3] = 3
answer = 0
least_prime = leastPrimeFactor(r)
exp = [1]*(r-l+1)
for i in range(1, len(exp)):
	exp[i]*=exp[i-1]*t
	exp[i]%=10**9 + 7
for i in range(4, len(dp)):
	dp[i] = f(i)
for i in range(r-l + 1):
	answer+= exp[i]* dp[l+i]
	answer%=10**9 + 7
print(answer)