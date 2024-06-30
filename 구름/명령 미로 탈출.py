# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n,m = map(int,input().split())
op = list(input())
li = []
dic = {
	'U' : [-1,0],
	'D' : [1,0],
	'L': [0,-1],
	'R' : [0,1],
}
x,y = 0,0
isSuccess = False
for i in range(n) :
	now = list(map(int,input().split()))
	if 1 in now :
		x = i
		y = now.index(1)
	li.append(now)
cnt = 0
for i in op :
	nx,ny = x+dic[i][0],y+dic[i][1]
	if nx < 0 or ny < 0 or nx >= n or ny >= n or li[nx][ny] == 3  :
		continue
	elif li[nx][ny] == 2 :
		cnt += 1
		isSuccess = True
		break
	else :
		x,y = nx,ny
		cnt += 1
if isSuccess :
	print('SUCCESS',cnt)
else :
	print('FAIL')
