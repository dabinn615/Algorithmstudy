lst=[[0 for _ in range (100)] for _ in range (100)] 

k=int(input(""))
for _ in range (k):
    a,b=input("").split(" ")
    a=int(a); b=int(b)
    for i in range (b,b+10):
        for j in range (a,a+10):
            lst[i][j]="1"
cnt=0
for i in lst:
    for j in i:
        if j=="1":
            cnt+=1
        else:
            pass
print(cnt)
