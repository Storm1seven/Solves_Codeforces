n = int(input())
large = []
l = []
small = []
for i in range (2*n -2):
    a = input()
    if len(a)== n-1:
        large.append(a)
    l.append(a)
    if len(a) <= 2:
        small.append(a)
a,b = large
word = ''
if a[:-1] == b [1:] and b[0] in small and b[0:2] in large:
    word = b[0] + a
else:
    word = a[0] + b
d = {}
for i in l:
    if word.startswith(i) and not(len(i) in d):
        print('P', end = '')
        d[len(i)] = 0
    else:
        print('S', end = '')