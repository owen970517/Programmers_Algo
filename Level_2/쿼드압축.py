def solution(arr) :
    answer = [0,0]
    l = len(arr)
    def quad(x,y,l) :
        now = arr[x][y]
        for i in range(x,x+l) :
            for j in range(y,y+l) :
                if arr[i][j] != now :
                    quad(x,y,l//2)
                    quad(x,y+(l//2),l//2)
                    quad(x+(l//2),y,l//2)
                    quad(x+(l//2),y+(l//2),l//2)
                    return 
        answer[now] += 1
    quad(0,0,l)
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))