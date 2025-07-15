def test9(a):
    if (a%100!=0 and a%4==0) or a%400==0:
        return "YES"
    else:
        return "NO"
