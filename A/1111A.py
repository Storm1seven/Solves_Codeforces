s = input()
t = input()
if len(s) == len(t):
    key = 'aeiou'
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        elif s[i] in key and t[i] in key:
            continue
        elif s[i] not in key and t[i] not in key:
            continue
        else:
            print('No')
            exit()
    print('Yes')
else:
    print('No')