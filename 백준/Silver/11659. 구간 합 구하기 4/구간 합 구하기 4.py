# 백준 11659 구간 합 구하기 4
import sys
read = sys.stdin.readline

num_cnt, oper_cnt = map(int,read().split())
nums = [0] + list(map(int,read().split()))
dp = [0] * (num_cnt + 1)

for i in range(1, num_cnt + 1):
    dp[i] = dp[i-1] + nums[i]

for _ in range(oper_cnt):
    a,b = map(int,read().split())
    print(dp[b] - dp[a-1])