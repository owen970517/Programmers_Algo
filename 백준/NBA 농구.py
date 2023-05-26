n = int(input())
now = 0
now_time = 0
dic = {
    '1' : '00:00',
    '2' : '00:00',
}
fullTime = 2880
for i in range(n) :
    team,time = input().split()
    m,s = map(int,time.split(':'))
    if i == 0 :
        prev = team
        prev_time = time
    