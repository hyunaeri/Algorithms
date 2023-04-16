# 백준 10103 주사위 게임
import sys
read = sys.stdin.readline

round = int(read())
a = 100
b = 100

for _ in range(round):
    c,d = map(int,read().split())
    if c > d:
        b -= c
    elif c < d:
        a -= d

print(a, b, sep='\n')

