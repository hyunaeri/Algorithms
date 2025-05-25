# 2025.05.25 (일)
# 백준 10815 숫자 카드
# 실버 5

import sys
read = sys.stdin.readline

# 숫자 카드의 개수
N = int(read())
cards = list(map(int, read().split()))
cards.sort()

# 가지고 있는 카드인지 확인할 횟수
M = int(read())
check = list(map(int, read().split()))

def binary_search(target):
  start, end = 0, len(cards) - 1
  
  while start <= end:
    mid = (start + end) // 2
    
    if target == cards[mid]: return 1
    elif target < cards[mid]: end = mid - 1
    elif target > cards[mid]: start = mid + 1
      
  return 0

for check_num in check:
  print(binary_search(check_num), end=' ')