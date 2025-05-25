# 2025.05.25 (일)
# 백준 15652 N과 M (8)
# 실버 3

import sys
read = sys.stdin.readline

# N개의 자연수 중에서 M개를 고른 수열
# 중복 가능
# 비 내림차순
N, M = map(int, read().split())

numbers = list(map(int, read().split()))
numbers.sort()

result = []

def backtracking(start):
  if len(result) == M:
    print(*result)
    return
  
  for i in range(start, len(numbers)):
    result.append(numbers[i])
    backtracking(i)
    result.pop()

backtracking(0)