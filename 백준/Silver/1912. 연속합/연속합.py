# 백준 1912 연속합
import sys
read = sys.stdin.readline

n = int(read())
num = list(map(int, read().rstrip().split()))
dp = num[:]

for i in range(1,n):
    dp[i] = max(num[i], dp[i-1]+ num[i])

print(max(dp))
