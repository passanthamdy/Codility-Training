"""
link
"""
def solution(n):
    i=p=0
    while 2 **i <=n:
        if n%2**i ==0:
            p=i
        i+=1

    return p

print(2%2)
print(solution(2))