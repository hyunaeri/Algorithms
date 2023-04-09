# 백준 4134 다음 소수
import sys
read = sys.stdin.readline

def prime_num(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2,int(n**0.5)+1,1):
            if n % i == 0:
                return False
        return True

T = int(read())
for _ in range(T):
    num = int(read())
    result = num
    while True: 
        if prime_num(result) == True:
            print(result)
            break
        else:
            result += 1