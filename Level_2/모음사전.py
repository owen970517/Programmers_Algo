import itertools

def solution(word):
    answer =''
    word_list = ['A','E','I','O','U']
    result = []
    for i in range(1,len(word_list)+1) :
        nPr = itertools.product(word_list , repeat=i)
        nPr = list(nPr)
        for i in nPr :
            result.append(''.join(i))
        result.sort()
    answer = result.index(word)+1
    return answer

print(solution('AAAAE'))