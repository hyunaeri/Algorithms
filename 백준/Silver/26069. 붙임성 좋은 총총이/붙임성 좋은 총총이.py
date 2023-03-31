# 백준 26069 붙임성 좋은 총총이
import sys
read = sys.stdin.readline

n = int(read())
rainbow = set()
rainbow.add('ChongChong')

for _ in range(n):
    a,b = read().rstrip().split()
    if a in rainbow :
        rainbow.add(b)
    elif b in rainbow:
        rainbow.add(a)
    else:
        continue
        
print(len(rainbow))

