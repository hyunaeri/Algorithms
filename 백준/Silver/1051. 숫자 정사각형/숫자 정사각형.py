import sys
read = sys.stdin.readline

N,M = map(int,read().split())
square = [ list(map(int,read().rstrip())) for _ in range(N) ]

# 정사각형의 넓이 구하는 함수
def area(x):
    return x**2

def find_square(x):
    for i in range(N-x+1):
        for j in range(M-x+1):
            if square[i][j] == square[i+x-1][j] == square[i][j+x-1] == square[i+x-1][j+x-1]:
                return True
            
    return False

size = min(N,M)

for i in range(size, 0 , -1):
    if find_square(i):
        print(area(i))
        break