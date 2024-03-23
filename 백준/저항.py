li = []
color = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9
}
ans = ''
for i in range(3) :
    now = input()
    if i < 2 :
        ans += str(color[now])
    else :
        ans += ('0'*color[now])
print(int(ans))