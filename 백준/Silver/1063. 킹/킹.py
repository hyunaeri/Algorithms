# 백준 1063 킹
# ord() : 문자를 아스키 코드로
# chr() : 아스키 코드를 문자로
import sys
read = sys.stdin.readline

# 이동방향
move = { 'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1] }

# A는 아스키코드로 65
king, stone, N = read().rstrip().split()
k = list(map(int, [ord(king[0]) - 64, king[1]]))
s = list(map(int, [ord(stone[0]) - 64, stone[1]]))

for _ in range(int(N)):
    command = read().rstrip()
    nx = k[0] + move[command][0]
    ny = k[1] + move[command][1]

    # 이동한 왕의 위치가 보드판 범위를 안 벗어나면,
    if 0 < nx < 9 and 0 < ny < 9:
        # 이동한 왕의 위치가 돌의 위치와 같으면,
        if nx == s[0] and ny == s[1]:
            sx = s[0] + move[command][0]
            sy = s[1] + move[command][1]
            # 이동한 돌의 위치가 보드판 범위를 안 벗어나면,
            if 0 < sx < 9 and 0 < sy < 9:
                k = [nx,ny]
                s = [sx,sy]
        
        else:
            k = [nx,ny]

print(chr(k[0] + 64), k[1], sep = '')
print(chr(s[0] + 64), s[1], sep = '')
