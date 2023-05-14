def solution(n, words):
    answer = []
    check = set()
    words.reverse()

    # 첫 단어의 마지막 글자 담아두기
    word = words.pop()
    check.add(word)
    prior = word[-1]

    person_idx = 2
    total = 1

    while words:
        # 이전단어의 마지막 글자와 현재단어의 첫 글자가 같다면, 끝말잇기 성립
        if prior == words[-1][0]:
            # 현재 단어가 나온적이 없다면,
            if not words[-1] in check:
                word = words.pop()
                check.add(word)
                prior = word[-1]

                if (person_idx + 1) > n:
                    person_idx = 1
                    total += 1
                else:
                    person_idx += 1
            # 현재 단어가 나온적이 있다면?
            else:
                answer.append(person_idx)
                answer.append(total)
                break
        
        # 다르다면?
        else:
            answer.append(person_idx)
            answer.append(total)
            break

    if len(answer) == 0:
        return [0,0]

    return answer
