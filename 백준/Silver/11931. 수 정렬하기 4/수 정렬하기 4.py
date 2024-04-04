# 백준 11931 수 정렬하기 4
# https://www.acmicpc.net/problem/11931
# 병합 정렬을 이용

import sys
read = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 배열을 2등분
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    
    # 병합
    left = merge_sort(L)
    right = merge_sort(R)
    
    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    ret_arr = []
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            ret_arr.append(left[i])
            i += 1
            
        else:
            ret_arr.append(right[j])
            j += 1
            
    # 남는 원소들 나열
    while i < len(left):
        ret_arr.append(left[i])
        i += 1
        
    while j < len(right):
        ret_arr.append(right[j])
        j += 1
        
    return ret_arr

# 수의 개수
N = int(read())
num = []

for _ in range(N):
    num.append(int(read()))
    
# print(num)

answer = merge_sort(num)

for a in answer:
    print(a)

