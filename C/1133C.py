n=int(input())
a=list(map(int,input().split()))
a.sort()
m, i, j = 0, 0, 0
while j<n:
 while a[j]-a[i]<=5:
     j+=1
     if j == n:
          break
 m=max(m,j-i)
 i+=1
print(m)