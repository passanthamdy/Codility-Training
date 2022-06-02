"""
Problem link
https://app.codility.com/programmers/trainings/4/first_unique/
"""
# lst = [4, 10, 5, 4, 2, 10]
# notU=[]

# for i in range(len(lst)-1):
#     el=lst[i]
#     c=0
#     for j in range(i+1,len(lst)):
#         if el==lst[j]:
#             c+=1
#     if c >0:
#         notU.append(el)
#
# for i in lst[:]:
#     if i in notU:
#          lst.remove(i)
# print(lst[0])


def solution(lst):
    # write your code in Python 3.6
    notU=[]
    for i in range(len(lst)-1):
        el=lst[i]
        c=0
        for j in range(i+1,len(lst)):
            if el==lst[j]:
                c+=1
        if c >0:
            notU.append(el)

    for i in lst[:]:
        if i in notU:
            lst.remove(i)
    if lst:
        return lst[0]
    else:
        return -1
lst =  [6, 4, 4, 6]
print(solution(lst))