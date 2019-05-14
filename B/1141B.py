n = int(input())
a = list(map(int, input().split()))
count = 0
mcount = 0
for i in range(2*n-1):
    if a[i%n] == 1:
        count+=1
    else:
        mcount = max(count, mcount)
        count = 0
print(mcount)