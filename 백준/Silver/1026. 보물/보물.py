# 백준 1026 보물
# https://www.acmicpc.net/problem/1026

import sys
read = sys.stdin.readline

# 배열의 길이
N = int(read())

arr_a = sorted(list(map(int, read().split())), reverse=True)
arr_b = list(map(int, read().split()))
dict_b = {}
for idx, num in enumerate(sorted(arr_b)):
    dict_b[idx] = num

S = 0

for i in range(len(arr_a)):
    S += arr_a[i] * dict_b[i]
    
print(S)

