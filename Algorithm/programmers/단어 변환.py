answer=0
def dfs(begin,target,words,visit):
    global answer
    stacks=[begin]
    while stacks:
        stack=stacks.pop()
        if stack==target:
            return answer
        for w in range(0,len(words)):
            if len([i for i in range(0,len(words[w])) if words[w][i]!=stack[i]])==1:
                # if visit[w]!=0:
                #     continue
                visit[w]=1
                stacks.append(words[w])
        answer+=1
def solution(begin,target,words):
    global answer
    if target not in words:
        return 0
    visit=[0 for i in words]
    dfs(begin,target,words,visit)
    return answer