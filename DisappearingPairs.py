import datetime
def solution(s):
    s=list(s)
    ln=len(s)
    removed=[]
    i=0
    while ln != 0 and i<ln-1 :
        if s[i]==s[i+1]:
            s=s[:i] + s[i+2 :]
            # s = s[:i] + s[i + 1:]
            # print('every loop ', s)
            ln-=2
            i=0
        else:
            i+=1

    return ''.join(s)



start_time = datetime.datetime.now()
print(solution('AABBCC'))
end_time = datetime.datetime.now()
print(end_time - start_time)