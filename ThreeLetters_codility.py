"""

"""
def solution(a,b):

    # s1 = list(s1)
    cntr=1
    if a==b:
        s1=''
        for i in range(a):
            s1+='ab'
    else:
        if a>b:
            s1 = ('a' * a) + ('b' * b)

        else:
            s1 = ('b' * b) + ('a' * a)
        s1=list(s1)
        for i in range(len(s1)):
            cntr = 1
            for k in range(len(s1)-1 ):
               # print(s1[k] , s1[k + 1],cntr)
                if s1[k] == s1[k + 1]:
                    cntr += 1
                else:
                    if cntr >= 3:
                        s1[k], s1[k + 1] = s1[k + 1], s1[k]
                        break;
                    else:
                        cntr = 1

    return ''.join(s1)



print(solution(3,5))




