def solution(nodeinfo) :
    answer = []
    dic = {}
    tree = {
        1 : ['.',8],
        2 : ['.',3],
        3 : ['.','.'],
        4 : [6,1],
        5 : ['.','.'],
        6 : ['.',9],
        7: [4,2],
        8 : [5,'.'],
        9 : ['.','.']
    }
    li = sorted(nodeinfo,key=lambda x:(-x[1],x[0]))
    dic[nodeinfo.index(li[0]) + 1] = []
    print(li)
    for i in range(1,len(li)) :
        for j in dic :
            print(li[i],li[i-1])
            if len(dic[j]) < 2 and li[i-1][1] > li[i][1]:
                dic[j].append(nodeinfo.index(li[i])+1)
        dic[nodeinfo.index(li[i]) + 1] = []

    print(dic)
    def preorder(root,li) :
        if root != '.' :
            li.append(root)
            preorder(tree[root][0],li)
            preorder(tree[root][1],li)
    def postorder(root,li) :
        if root != '.' :
            postorder(tree[root][0],li)
            postorder(tree[root][1],li)
            li.append(root)
    pre = []
    post = []
    preorder(nodeinfo.index(li[0])+1,pre)
    print()
    postorder(nodeinfo.index(li[0])+1,post)
    answer.append(pre)
    answer.append(post)
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))