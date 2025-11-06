# 백준 10816
# 실버 4
# https://www.acmicpc.net/problem/10816

import sys
read = sys.stdin.readline

# 숫자 카드의 개수
N = int(read())

# 카드 정보
card = list(map(int, read().rstrip().split()))
dic_card = dict()

for c in card:
  if c not in dic_card:
    dic_card[c] = 1
  
  else: dic_card[c] += 1

# 찾아야 할 카드 정보
M = int(read())
target = list(map(int, read().rstrip().split()))

for t in target:
  print(0 if t not in dic_card else dic_card[t], end=' ')
