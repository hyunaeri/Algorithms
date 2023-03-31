def solution(nums):
    # 중복 제거
    n = set(nums)
    # 가질 수 있는 포켓몬 마릿 수
    s = len(nums)//2

    if s < len(n):
        return s
    else:
        return len(n)