def solution(progresses, speeds):
    answer = []
    lst=[]
    cnt=0
    for i in range (len(progresses)):
        if (100-progresses[i])%speeds[i]==0:
            lst.append((100-progresses[i])//speeds[i])
        else:
            lst.append(((100-progresses[i])//speeds[i]+1))
    maxx=lst[0]
    for i in range (len(lst)):
            if lst[i]<=maxx:
                cnt+=1
                if i==len(lst)-1:
                    if maxx<lst[i]:
                        answer.append(1)
                    else:
                        answer.append(cnt)
            elif lst[i]>maxx:
                if i==len(lst)-1:
                    if maxx<lst[i]:
                        answer.append(cnt)
                        answer.append(1)
                else:  
                    maxx=lst[i]
                    answer.append(cnt)
                    cnt=1
    return answer
