def solution(n):
    binary=format(n, "b")
    print(binary)
    gaps=[]
    max = 0
    for i in range(len(binary)):
        if binary[i]=='1':
            gaps.append(i)
    if gaps:
        for i in range(len(gaps)-1):

            if gaps[i+1]-gaps[i] >max:
                max=gaps[i+1]-gaps[i]
    if max==0:
        return 0
    else:
        return max-1



print(solution(32))
