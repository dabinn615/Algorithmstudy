a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
lst1=[a,c,e]
lst2=[b,d,f]
for i in lst1:
    if a==c:
        for j in lst2:
            if b==d:
                print(e,f)
                break
            elif d==f:
                print(e,b)
                break
            elif f==b:
                print(e,d)
                break
        break
    elif c==e:
        for j in lst2:
            if b==d:
                print(a,f)
                break
            elif d==f:
                print(a,b)
                break
            elif f==b:
                print(a,d)
                break
        break
    elif e==a:
        for j in lst2:
            if b==d:
                print(c,f)
                break
            elif d==f:
                print(c,b)
                break
            elif f==b:
                print(c,d)
                break
        break
