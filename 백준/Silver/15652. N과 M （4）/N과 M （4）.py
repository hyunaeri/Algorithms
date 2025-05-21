# 2025.05.21 (수)
# 백준 15652 N과 M (4)
# 실버 3

import sys
read = sys.stdin.readline

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 중복 가능
# 고른 수열은 비 내림차순
N, M = map(int, read().split())

result = []

def backtracking(start):
  if len(result) == M:
    print(*result)
    return

  for num in range(start, N + 1):
    result.append(num)
    backtracking(num)
    result.pop()
      
backtracking(1)