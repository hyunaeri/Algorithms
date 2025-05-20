# 2025.05.20 (화)
# 백준 18406 럭키 스트레이트
# 브론즈 2

import sys
read = sys.stdin.readline

N = int(read())
str_n = list(str(N))
mid_index = len(str_n) // 2

front = list(map(int, str_n[:mid_index]))
rear = list(map(int, str_n[mid_index:]))

print('LUCKY' if sum(front) == sum(rear) else 'READY')