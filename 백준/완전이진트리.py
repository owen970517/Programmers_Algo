def binary_tree(li,depth) : 
    root_index = (len(li)//2)
    tree[depth].append(li[root_index])
    if len(li) == 1 :
        return
    binary_tree(li[:root_index],depth+1)
    binary_tree(li[root_index+1:],depth+1)
    
k = int(input())
li = list(map(int,input().split()))
tree = [[] for _ in range(k)]
binary_tree(li,0)
for i in range(len(tree)) :
    print(*tree[i])