# calendar 라이브러리 사용
import calendar
def solution(a, b):
    answer = ''
    week = ["MON" ,"TUE" , "WED" , "THU" , "FRI" , "SAT","SUN"]
    week_idx = calendar.weekday(2016,a,b)
    answer = week[week_idx]
    return answer

a,b = map(int,input().split())
print(solution(a,b))

""" 내가 푼 답 
def solution(a, b):
    answer = ''
    sum=0
    week = ["SUN", "MON" ,"TUE" , "WED" , "THU" , "FRI" , "SAT"]
    now_week = week[5]
    now_week_idx = week.index("FRI")
    days=[31,29,30,31,30,31,30,31,30,31,30,31]
    for i in range(a-1):
        sum +=days[i]
    sum +=b
    day = sum%7
    if day ==0 :
        answer=now_week
    now_week_idx +=day
    if now_week_idx > 7:
        now_week_idx-=7
        answer=week[now_week_idx-1]
    else:
        answer=week[now_week_idx-1]
    return answer """