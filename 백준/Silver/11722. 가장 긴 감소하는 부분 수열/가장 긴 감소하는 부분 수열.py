# 백준 11722 가장 긴 감소하는 부분 수열
from sys import stdin
read = stdin.readline

N = int(read())
a = list(map(int,read().split()))
dp = [1] * (N)

for i in range(1, N):
    for j in range(i):
        if a[j] > a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))