"""
https://app.codility.com/c/run/trainingWZKJ43-ZWV/
"""
def solution(enternce,leaving):

    #leaving-enterance
    lst1=enternce.split(':')
    lst2=leaving.split(':')
    leaving_hours=int(lst2[0])
    leaving_mins=int(lst2[1])
    enternce_hours=int(lst1[0])
    enternce_mins=int(lst1[1])
    hours=fees=0

    if leaving_hours<enternce_hours:
        hours=abs((enternce_hours-leaving_hours)-24)
    else:
        hours=abs((enternce_hours-leaving_hours))

    if leaving_mins>enternce_mins:
        hours+=1
    print('hours: ', hours)
    if hours == 1:
        fees=5
    elif hours==0:
        fees= 0
    else:
        fees=((hours-1)*4)+5

    return fees

print(solution('00:00', '00:59'))