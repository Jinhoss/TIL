import datetime

def solution(a, b):
    day=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    i=datetime.date(2016,a,b).weekday()
    answer = day[i]
    
    return answer