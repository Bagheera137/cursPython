def test11(a,b,c,d):
    if abs((a-c)==1) and abs((b-d)==2):
        return "YES"
    elif abs((a-c)==2) and abs((b-d)==1):
        return "YES"
    else:
        return "NO"

