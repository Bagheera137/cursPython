def test10(n,m,x,y):
    if m>n:
        n,m=m,n
    a=m-x
    b=n-y
    if a>x:
        a,x=x,a
    if b>y:
        b,y=y,b
    if a>b:
        return b
    else:
        return a






