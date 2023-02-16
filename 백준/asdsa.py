dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six',
        '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
n,m = map(int,input().split())
arr = []
for i in range(n,m+1) :
    li=[]
    for j in str(i) :
        li.append(dict[j])
    now = ' '.join(li)
    arr.append([i,now])
arr.sort(key=lambda x:x[1])
for i in range(len(arr)) :
    if i % 10 == 0 and i != 0:
        print(sep='\n')
    print(arr[i][0] , end=' ')

