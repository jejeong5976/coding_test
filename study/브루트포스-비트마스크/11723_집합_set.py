import sys
input = sys.stdin.readline

M = int(input())
s = set()

for i in range(M):
    computation = list(map(str,input().strip().split()))
    
    if len(computation)==1:
        comp = computation[0]
    else:
        comp, x = computation[0], int(computation[1])
    
    if comp=='add':
        s.add(x)
    elif comp == 'remove':
        s.discard(x)
    elif comp == 'check':
        print(1 if x in s else 0)
    elif comp == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif comp == 'all':
        s = set(range(1,21))
    elif comp == 'empty':
        s.clear()


