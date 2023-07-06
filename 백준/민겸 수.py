s = input()
m_cnt = 0
max_ans, min_ans ='',''

for i in s :
    if i == 'M' :
        m_cnt+= 1
    else :
        if m_cnt > 0 :
            max_ans += str(5*(10**m_cnt))
            min_ans += str(10**m_cnt+5)
            m_cnt = 0
        else :
            max_ans +='5'
            min_ans +='5'
if m_cnt> 0 :
    max_ans += '1'*m_cnt
    min_ans += str(10**(m_cnt-1))

print(max_ans)
print(min_ans)

        