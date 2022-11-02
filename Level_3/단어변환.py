from collections import deque

def bfs(begin,target,words,visited) :
    queue = deque()
    queue.append([begin,0])
    while queue :
        word,cnt = queue.popleft()
        if word == target :
            return cnt
        print(word)
        for i in range(len(words)) :
            diff_cnt = 0
            if not visited[i] :
                for j in range(len(word)):
                    if word[j] != words[i][j] :
                        diff_cnt += 1
                if diff_cnt == 1 :
                    queue.append([words[i],cnt+1])
                    visited[i] = 1

def solution(begin,target,words) :
    answer = ''
    if target not in words :
        return 0
    visited = [0] * len(words)
    answer = bfs(begin,target,words,visited)
    return answer

print(solution('hit','cog',	["hot", "dot", "dog", "lot", "log", "cog"]))