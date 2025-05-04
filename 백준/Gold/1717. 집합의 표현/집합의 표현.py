# 2025.05.04 (일)
# 백준 1717 집합의 표현
# 골드 5

import sys
read = sys.stdin.readline

# 집합의 개수 + 1, 연산의 개수
n, m = map(int, read().split())
parent = [i for i in range(n + 1)]

def find(x):
  while parent[x] != x:
    parent[x] = parent[parent[x]]
    x = parent[x]
  return x

def union(x, y):
  parent_x = find(x)
  parent_y = find(y)
  
  if parent_x == parent_y:
    return
  
  if parent_x > parent_y:
    parent[parent_x] = parent_y
  else:
    parent[parent_y] = parent_x

for _ in range(m):
  command, a, b = map(int, read().split())
  
  # 합집합
  if command == 0:
    union(a, b)
    
  # 같은 집합인지 확인
  else:
    if find(a) == find(b):
      print('YES')
    else:
      print('NO')  