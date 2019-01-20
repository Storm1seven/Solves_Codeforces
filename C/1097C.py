def valid(s):
    stack = []
    for c in s:
        if c =='(':
            stack.append(c)
        elif c ==')':
            if not stack or stack[-1] != ')':
            	stack.pop()
            	stack.append(c)
    return stack
n = int(input())
a = []
for _ in range(n):
	a.append(valid(input()))
print(a)