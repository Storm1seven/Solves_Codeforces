from collections import defaultdict, deque
from bisect import insort
from sys import stdin, stdout
input = stdin.readline
print = stdout.write
n, m = map(int, input().split())
d = defaultdict(list)
visited = [False]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    insort(d[u], v)
    insort(d[v], u)
z = deque([1])
visited[1] = True
while z:
    front = z.popleft()
    print(str(front)+' ')
    for i in d[front]:
        if not visited[i]:
            insort(z, i)
            visited[i] = True