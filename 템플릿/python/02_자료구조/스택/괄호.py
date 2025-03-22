def check_patern(word):
    stack = []
    for w in word:
        if w == '(':
            stack.append(w)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    return True


def word_split(word_all):
    good = []
    bad = []
    print(word_all)


def solution(word):
    good, bad = word_split(word)
    print(good)
    print(bad)
    answer = 0
    return answer


print(solution("(()())()"))
# print(solution(")("))
# print(solution("()))((()"))
