# 백준 11053 가장 긴 증가하는 수열(Longest Increasing Subsequence)
import sys
read = sys.stdin.readline

n = int(read().rstrip())
a = list(map(int,read().rstrip().split()))

# n[i]를 포함한 수열의 길이를 담아 놓을 리스트
LIS = [ 1 for _ in range(n) ]

for i in range(1,n):
    for j in range(i):
        if a[i] > a[j]:
            LIS[i] = max(LIS[i], LIS[j]+1)

print(max(LIS))

