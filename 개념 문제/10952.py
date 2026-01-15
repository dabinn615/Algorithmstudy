while 1:
    a,b=map(int,input("").split())
    if a!=0 and b!=0:
        print(a+b)
    elif a==0 and b==0:
        break
    if a==0 or b==0:
        if a==0:
            print(b)
        else:
            print(a)
