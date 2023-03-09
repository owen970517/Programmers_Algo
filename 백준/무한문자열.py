s = input()
t=input()
if s not in t and t not in s :
    print(0)
else :
    if s * len(t) == t * len(s) :
        print(1)