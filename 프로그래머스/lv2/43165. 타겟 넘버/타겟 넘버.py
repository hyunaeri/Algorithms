def solution(numbers, target):
    idx = sum = 0
    
    def dfs(numbers, target, sum, idx):
        if idx == len(numbers):
            return 1 if sum == target else 0
        
        return dfs(numbers, target, sum + numbers[idx], idx + 1) \
                + dfs(numbers, target, sum - numbers[idx], idx + 1)
    
    answer = dfs(numbers, target, sum, idx)
    return answer