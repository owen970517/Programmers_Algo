import re

s = input()
answer = ''
for i in s :
    if i.islower() == True or i == ' ' :
        continue
    else :
        answer += i
if answer == 'UCPC' :
    print('I love UCPC')
elif len(answer) > 4 :
    for i in range(len(answer)) :
        if answer[i:i+4] == 'UCPC' :
            print('I love UCPC')
            break
        else :
            print('I hate UCPC')
else :
    print('I hate UCPC')


# new_text = re.sub(r"[a-z]", "", s)
# for i in new_text :
#     if i != ' ' :
#         answer +=i
# if answer == 'UCPC' :
#     print('I love UCPC')
# else :
#     print('I hate UCPC')