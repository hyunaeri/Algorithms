# 백준 11055 가장 큰 증가하는 부분 수열
import sys
read = sys.stdin.readline

n = int(read().rstrip())
a = list(map(int, read().rstrip().split()))

dp = [ 0 for _ in range(n) ]

for i in range(n):
    dp[i] = a[i]
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))