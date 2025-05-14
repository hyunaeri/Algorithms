# 2025.05.14 (수)
# 백준 15650 N과 M (2)
# 실버 3

import sys
read = sys.stdin.readline

# 1 ~ N 까지의 자연수 중에서 중복 없이 M개를 고른 수열 (오름차순)
N, M = map(int, read().split())
visited = [False] * (N + 1)
result = []

def backtracking(start):
  if len(result) == M:
    print(' '.join(map(str, result)))
    return
  
  for i in range(start, N + 1):
    if not visited[i]:
      visited[i] = True
      result.append(i)
      backtracking(i + 1)
      result.pop()
      visited[i] = False
    
backtracking(1)