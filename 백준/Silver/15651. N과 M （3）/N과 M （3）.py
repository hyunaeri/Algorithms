# 2025.05.13 (화)
# 백준 15649 N과 M (3)
# 실버 3

import sys
read = sys.stdin.readline

# 1부터 N까지의 자연수 중에서 M개를 고른 수열 (같은 수 여러번 가능)
N, M = map(int, read().split())
arr = []

def backtracking():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N + 1):
        arr.append(i)
        backtracking()
        arr.pop()

backtracking()