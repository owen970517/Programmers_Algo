import re

s = input()
k = input()
new_s = re.sub(r"[0-9]", "", s)
print(new_s)

if k in new_s :
    print(1)
else :
    print(0)
# for i in k :
#     print(s.index(i))