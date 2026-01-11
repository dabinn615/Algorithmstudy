lst=[]
for i in range (9):
    nums=input("").split(" ")
    for j in range (9):
        lst.append(int(nums[j]))
print(max(lst))
max=max(lst)
cnt=0
for i in lst:
    if i==max:
        print(cnt//9+1,cnt%9+1)
        break
    else:
        cnt+=1
