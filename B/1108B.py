n = int(input())
a = list(map(int, input().split()))
num1 = max(a)
m = 0
d = set([])
for i in a:
    if a.count(i) >= 2:
        d.add(i)
    elif num1%i!=0:
        d.add(i)
print(num1, max(list(d)))