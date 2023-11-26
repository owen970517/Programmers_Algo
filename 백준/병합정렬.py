def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = (len(arr)+1) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    merged_arr = []
    l,h= 0,0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            res.append(low_arr[l])
            merged_arr.append(low_arr[l])
            l += 1
        else:
            res.append(high_arr[h])
            merged_arr.append(high_arr[h])
            h += 1
    while l < len(low_arr):
        merged_arr.append(low_arr[l])
        res.append(low_arr[l])
        l+=1
    while h < len(high_arr):
        merged_arr.append(high_arr[h])
        res.append(high_arr[h])
        h+=1

    return merged_arr

n,k = map(int,input().split())
li = list(map(int,input().split()))
res = []

merge_sort(li)
if k > len(res) :
    print(-1)
else :
    print(res[k-1])