def solution(priorities, location):
    answer = 0
    lst=[]
    cnt=0

    for i in priorities:
        lst.append((i,cnt))
        cnt+=1

    total=[]
    while 1:
        maxnum=max(priorities)
        for i in range(len(lst)):
            if lst[i][0]==maxnum:
                total.append(lst[i])
                priorities.remove(lst[i][0])
                lst=lst[(i+1):]+lst[:i]
                break
                
        if len(priorities)==0:
            break

    for i in total:
        if i[1]==location:
            answer=(answer+1)
            break
        else:
            answer+=1
    return answer

priorities=[int(i) for i in input("").split(",")]
location=int(input("")) #배열의 자리 위치
print(solution(priorities, location))
