# 2025.05.14 (수)
# 백준 1182 부분수열의 합
# 실버 2

import sys
read = sys.stdin.readline

# 정수의 개수, 부분수열의 합
N, S = map(int, read().split())

# 수열, 부분 수열
arr = list(map(int, read().split()))
partial_arr = []
answer = 0

def backtracking(start):
  global answer
  if len(partial_arr) > 0 and sum(partial_arr) == S:
    answer += 1
  
  for i in range(start, len(arr)):
    partial_arr.append(arr[i])
    backtracking(i + 1)
    partial_arr.pop()
    
backtracking(0)

print(answer)