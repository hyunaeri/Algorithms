# 백준 20920 영단어 암기는 괴로워
import sys
read = sys.stdin.readline

# 딕셔너리[키] : { [값(개수), 길이, 단어] }
words = dict()

# 단어의 개수, 기준이 되는 단어의 길이
n,m = map(int, read().rstrip().split())
for _ in range(n):
    word = read().rstrip()
    # 기준 미만이라면 단어장에 추가 X
    if len(word) < m:
        continue
    else:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

# 개수, 길이는 내림차순, 단어는 사전순(오름차순)
result = sorted(words.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
for r in result:
    print(r[0])