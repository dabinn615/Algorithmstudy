nm=input("").split(" ")
n=int(nm[0]); m=int(nm[1])
nums=input("").split(" ")
lst=[int(i) for i in nums]

sum=0
sumlst=[]
for i in lst:
    for j in lst:
        for k in lst:
            if i!=j and j!=k and k!=i:
                sum=(i+j+k)
                sumlst.append(sum)
            else:
                pass
sumlst=set(sumlst)                    

total=[]
cnt=0
for i in sumlst:
    if i==m:
        print(i)
        cnt+=1
    else: 
        if i<m:
            total.append(i)
        else:
            pass
if cnt==1:
    pass
else:
    total.sort()
    print(total[-1]) 
