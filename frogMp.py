def solution(x,y,d):
    result=0
    ds=y-x
    if ds % d ==0:
        result=ds//d
    else:
        result=(ds//d)+1

    print(result)


solution(1,1000000000,30)