# 백준 26069 붙임성 좋은 총총이
import sys
read = sys.stdin.readline

n = int(read())
rainbow = set()

for _ in range(n):
    a,b = read().rstrip().split()
    if a == 'ChongChong' or b == 'ChongChong':
        if a not in rainbow or b not in rainbow:
            rainbow.add(a)
            rainbow.add(b)
    else:
        if a in rainbow or b in rainbow:
            rainbow.add(a)
            rainbow.add(b)

print(len(rainbow))

