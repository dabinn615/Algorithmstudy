word=input("").upper().split()
lst=[i for i in word[0]]

setlst=set(lst)
setlst=list(setlst)

cnt=0
cntlst=[]
dic={}
for i in setlst:
    dic.update({i:lst.count(i)})

value=[]
for v in dic.values():
    value.append(v)

maxx=max(value)
if value.count(maxx)!=1:
    print("?")
else:
    for k,v in dic.items():
        if v==maxx:
            print(k)
        else:
            pass
