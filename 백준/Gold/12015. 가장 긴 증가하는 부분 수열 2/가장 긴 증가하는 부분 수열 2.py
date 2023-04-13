# 백준 12015 가장 긴 증가하는 부분 수열2
# 일반적인 LIS 알고리즘(dp)로 풀기에는 시간 복잡도가 O(n^2)이므로,,
# 이분 탐색을 통해 O(nlogn)으로 줄여서 풀어야한다
# 진짜 LIS는 아니다, 주의하자 
# 길이만 구하는 문제이기에 성립함

import sys
read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().rstrip().split()))
LIS = [nums[0]]

def binary_search(target):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] == target:
            return mid
        if LIS[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start

for n in nums:
    if LIS[-1] < n:
        LIS.append(n)
    else:
        LIS[binary_search(n)] = n

print(len(LIS))