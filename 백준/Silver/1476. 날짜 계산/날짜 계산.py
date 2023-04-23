# 백준 1476 날짜 계산
import sys
read = sys.stdin.readline

E,S,M = map(int,read().split())
e,s,m,answer = 1,1,1,1

while True:
    if E == e and S == s and M == m:
        break
    
    e += 1
    s += 1
    m += 1
    answer += 1

    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1

print(answer)
