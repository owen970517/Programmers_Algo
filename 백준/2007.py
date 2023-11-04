x,y = map(int,input().split())
week = ['MON','TUE','WED','THU','FRI','SAT','SUN']
day = [31,28,31,30,31,30,31,31,30,31,30,31]
s = 0
a= x-1
b=y-1
s = (sum(day[:a]) + b)%7
print(week[s])

