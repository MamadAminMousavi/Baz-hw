def aval():
    m=0
    a=int(input())
    for i in range(a):
        b=int(input())
        if b%2==0 or b%3==0 :
            
            m=1+m
    return m



print(aval())