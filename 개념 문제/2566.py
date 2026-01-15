lst=[]
for i in range (9):
    nums=input("").split(" ")
    for j in range (9):
        lst.append(int(nums[j]))

maxnum=lst[0]
for i in lst:
    if i>maxnum:
        maxnum=i
print(maxnum)

cnt=0
for i in lst:
    if i!=maxnum:
        cnt+=1
    else:
        print(cnt//9+1,cnt%9+1)
        break
