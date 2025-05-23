# 2025.05.23 (금)
# 백준 15654 N과 M(5)
# 실버 3

import sys
read = sys.stdin.readline

# N개의 자연수 중에서 M개를 고른 수열
# 중복 불가능
N, M = map(int, read().split())

# 선택할 수 있는 자연수 리스트
arr = list(map(int, read().split()))
arr.sort()

result = []
visited = [False] * N

def backtracking():
  if len(result) == M:
    print(*result)
    return
  
  for i in range(len(arr)):
    if not visited[i]:
      result.append(arr[i])
      visited[i] = True
      backtracking()
      result.pop()
      visited[i] = False

backtracking()