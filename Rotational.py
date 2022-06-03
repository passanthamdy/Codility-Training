"""
https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
"""

def solution(lst,k):

    for i in range(k):
        el=lst.pop()
        lst=[el]+lst


    return lst

lst=[]
k=6
print(solution(lst,k))

