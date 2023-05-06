# 백준 14002 가장 긴 증가하는 부분수열 4 (Longest Increasing Subsequence)
import sys
read = sys.stdin.readline

n = int(read().rstrip())
a = list(map(int,read().rstrip().split()))

def dfs(x):
    if x == -1:
        return
    
    dfs(path[x])
    print(a[x], end = ' ')

# n[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이를 담아 놓을 리스트
dp = [ 1 for _ in range(n) ]

# 역추적을 위한 경로 저장
# path[i] : dp[i] 최댓값이 갱신 될 당시 어느 인덱스로 부터 왔는지? 
path = [ -1 for _ in range(n) ]

for current in range(1, n):
    for prev in range(current):
        if a[prev] < a[current] and dp[current] < dp[prev] + 1:
            dp[current] = dp[prev] + 1
            path[current] = prev

ans = max(dp)
idx = dp.index(ans)
print(ans)
dfs(idx)