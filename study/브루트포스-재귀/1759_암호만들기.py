import sys

input = sys.stdin.readline
L, C = map(int,input().split())
char = list(input().strip().split())
char.sort()

result = []
def recur(start,depth):
    if depth == L:
        aeiou = 0
        not_aeiou = 0
        for r in result:
            if r in ['a','e','i','o','u']:
                aeiou+=1
            else:
                not_aeiou+=1
        if aeiou>=1 and not_aeiou>=2:
            print(''.join(result))
        return
    
    for i in range(start,C):
        result.append(char[i])
        recur(i+1,depth+1)
        result.pop()

recur(0,0)