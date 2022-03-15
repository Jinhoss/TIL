def check(word):
    stack = []
    for w in word:
        if w == '(':
            stack.append(w)
        elif w == ')':
            if not stack:
                return False
            elif stack.pop() != '(':
                return False
        elif w == '[':
            stack.append(w)
        elif w == ']':
            if not stack:
                return False
            elif stack.pop() != '[':
                return False
        elif w == '{':
            stack.append(w)
        else:
            if not stack:
                return False
            elif stack.pop() != '{':
                return False
    if len(stack):
        return False
    return True


def solution(s):
    answer = 0

    for i in range(len(s)):
        word = s[i:] + s[:i]
        if check(word):
            answer += 1
    return answer

if __name__ == '__main__':
    print(solution("[](){}"))