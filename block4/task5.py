
def test5(a,b,c):
    if a>b:
        a,b=b,a
    if b>c:
        b,c=c,b
        if a>b:
            a,b=b,a
    return [a,b,c]

if __name__=="__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(test5(a,b,c))