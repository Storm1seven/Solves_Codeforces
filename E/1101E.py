x = 0
y = 0
for _ in range(int(input())):
    s, a, b = input().split()
    a = int(a)
    b = int(b)
    if s == '+':
        x = max(x, min(a, b))
        y = max(y, max(a, b))
    else:
        if (a < x and a < y) or (b < x and b < y) :
            print('NO')
        else:
            print('YES')