# Summer / Winter Coding (~2018)
# 소수 만들기

def prime_number(num):
    if num < 2:
        return False

    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

def solution(nums):
    answer = 0

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for z in range(j+1, len(nums)):
                if prime_number(nums[i] + nums[j] + nums[z]):
                    answer += 1

    return answer
