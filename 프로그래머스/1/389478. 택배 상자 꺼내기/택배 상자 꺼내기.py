def removeBoxCalc(n, w, num):
    storage = []
    height = 0
    currentBox = 1
    answer = 0
    
    if (n % w == 0):
        height = n // w
    else:
        height = n // w + 1

    # 2차원 리스트(storage) 생성
    for level in range(height):
        currentLevel = []
        for _ in range(w):
            if currentBox <= n:
                currentLevel.append(currentBox)
                currentBox += 1
            else:
                currentLevel.append(0)

        # 짝수 층: 그대로 저장
        # 홀수 층: 뒤집어서 저장
        if level % 2 == 0:
            storage.append(currentLevel)
        else:
            currentLevel.reverse()
            storage.append(currentLevel)

    # 탐색
    for i in range(len(storage)):
        for j in range(w):
            if storage[i][j] == num:
                h = i
                while h < height and storage[h][j]:
                    answer += 1
                    h += 1

    return answer

def solution(n, w, num):
    return removeBoxCalc(n, w, num)