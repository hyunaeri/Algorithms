# 2025.05.20 (화)
# 백준 1920 수 찾기
# 실버 4

import sys
read = sys.stdin.readline

N = int(read())
arr = list(map(int, read().split()))
arr = sorted(arr)

M = int(read())
check = list(map(int, read().split()))

def binary_search(arr, target):
  start, end = 0, len(arr) - 1
  
  while start <= end:
    mid = (start + end) // 2
    
    if arr[mid] == target:
      return 1
      
    elif arr[mid] < target:
      start = mid + 1
      
    elif arr[mid] > target:
      end = mid - 1
  
  return 0

for num in check:
  print(binary_search(arr, num))

