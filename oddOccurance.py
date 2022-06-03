"""

"""
def solution(a):
    if len(a)==0:
        return 0
    elif len(a)==1:
        return a[0]
    else:
        a=sorted(a)
        c=1
        lst=[]
    for i in a:
        if i in lst:
            lst.remove(i)
        else:
            lst.append(i)
    return lst[0]


print(solution([5,2,5]))