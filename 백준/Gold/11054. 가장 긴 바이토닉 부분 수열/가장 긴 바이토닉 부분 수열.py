# 백준 11054 가장 긴 바이토닉 부분 수열
import sys
read = sys.stdin.readline

n = int(read())
array = list(map(int,read().split()))
increase = [1] * n
decrease = [1] * n

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            increase[i] = max(increase[i], increase[j]+1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if array[i] > array[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0] * n

for i in range(n):
    result[i] = increase[i] + decrease[i] - 1

print(max(result))
