x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
n = int(input())
s = input()
y_dist = y2 - y1
x_dist = x2 - x1
count = abs(y_dist)+abs(x_dist)
if y_dist > 0:
    y_dir = 'U'
elif y_dist < 0:
    y_dir = 'D'
else:
    y_dir = 'X'
if x_dist > 0:
    x_dir = 'R'
elif x_dist < 0:
    x_dir = 'L'
else:
    x_dir = 'X'
ans = 0
