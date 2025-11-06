# 백준 14719
# 골드 5
# https://www.acmicpc.net/problem/14719

import sys
read = sys.stdin.readline

if __name__ == "__main__":
  answer = 0
  
  # 2차원 세로, 가로 길이
  H, W = map(int, read().rstrip().split())
  
  # 블록이 쌓인 높이
  height = list(map(int, read().rstrip().split()))
  
  for i in range(1, W - 1):
    left = max(height[:i])
    right = max(height[i+1:])
    
    low_spot = min(left, right)
    
    # print(f"좌측 {left}, 우측 {right}, 현재 높이 {height[i]}")
    
    if height[i] < low_spot:
      answer += low_spot - height[i]
  
  print(answer)