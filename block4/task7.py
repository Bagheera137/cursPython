
def test7(n):
    if 10<n%100<20:
        return str(n)+" bochek"
    elif  n % 10 == 1:
        return str(n) + " bochka"
    elif n%10 in [2,3,4]:
        return str(n) + " bochki"
    else:
        return str(n) + " bochek"
if __name__=="__main__":
    a=int(input())
    result=test7(a)
    print(result)
