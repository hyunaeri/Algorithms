def solution(wallpaper):
    # 세로, 가로 길이
    H, W = len(wallpaper), len(wallpaper[0])
    
    # 파일 위치 다 찾아놓기 
    file = []
    for i in range(H):
        for j in range(W):
            if wallpaper[i][j] == '#':
                file.append([i,j])
                
    f1 = sorted(file, key = lambda x : x[0])
    # print(f1)
    f2 = sorted(file, key = lambda x : x[1])
    # print(f2)
    
    x1 = f1[0][0]
    x2 = f1[-1][0]
    y1 = f2[0][1]
    y2 = f2[-1][1]
    
    return [x1,y1,x2+1,y2+1]