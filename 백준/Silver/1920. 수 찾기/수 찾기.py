# 백준 1920 수 찾기
# 
import sys
read = sys.stdin.readline

N = int(read())
nums = list(map(int,read().split()))
nums = sorted(nums)

# 타겟
M = int(read())
target = list(map(int,read().split()))

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return 1

        elif nums[mid] > target:
            end = mid - 1
        
        elif nums[mid] < target:
            start = mid + 1

    return 0

for t in target:
    print(binary_search(t, 0, len(nums)-1))