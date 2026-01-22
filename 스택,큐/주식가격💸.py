def solution(prices):
    answer = []
    cnt=0
    for i in range(len(prices)):
        if i==len(prices)-1:
            answer.append(0)
        else:
            if prices[i]<=prices[i+1]:
                for j in range (i+1,len(prices)):
                    if prices[i]<=prices[j]:
                        cnt+=1
                        if cnt==len(prices)-i-1:
                            answer.append(cnt)
                            cnt=0
                    else:
                        answer.append(cnt+1)
                        cnt=0
                        break
            else:
                answer.append(1)
    return answer
    
prices=[int(i) for i in input("").split(",")]
print(solution(prices))
