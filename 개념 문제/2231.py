num=input("")
lenn=len(num)
num=int(num)
lst=[]
total=[]

for i in range (1,num+1):
    i=str(i)
    lst=[int(j) for j in i]
    i=int(i)
    if i+sum(lst)==num:
        total.append(i)

if len(total)!=0:
    print(total[0])
else:
    print("0")
