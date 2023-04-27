# 백준 1717 집합의 표현
import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

# n+1 개의 집합, m 개의 연산
n, m = map(int,read().split())
parent = [ i for i in range(n+1) ]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    px = find(x)
    py = find(y)

    if px == py:
        return
    
    if px > py:
        parent[px] = py
    else:
        parent[py] = px

# m 번의 연산
for _ in range(m):
    operator, a, b = map(int, read().split())

    if operator == 0:
        union(a,b)

    elif operator == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')