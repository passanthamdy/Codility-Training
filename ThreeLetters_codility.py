"""

"""

a=5
b=3
s1=('a'*a)+('b'*b)
s1=list(s1)
k=1
for i in range(len(s1)):
    next=0
    while s1[i]==s1[next]:
        print('while')
        if i==next:
            print('cont')
            next+=1
            continue
        else:
            print('next',next)
            next+=1
        if next>=3:
            print('swap',s1[next],next,s1[next+1],next+1)
            s1[i],s1[next]=s1[next],s1[i]
            print(s1)





