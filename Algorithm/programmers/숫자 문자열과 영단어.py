def solution(s):
    answer = ''
    word_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 
                'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    key = ''
    for word in s:
        if word.isdigit():
            answer += word
        else:
            key += word
            if key in word_dict.keys():
                answer += word_dict[key]
                key = ''
    return int(answer)