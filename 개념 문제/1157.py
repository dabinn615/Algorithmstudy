word=input("").upper().split()
lst=[i for i in word[0]]
#미리 리스트로 각 단어가 몇번 나와는지 만들어놓기!!

wordlst=[]
for i in range(len(lst)):
    cnt=lst.count(lst[i])
    if [lst[i],cnt] not in wordlst:
        wordlst.append([lst[i],cnt])

maxx=0
for i in wordlst:
    if i[1]>maxx:
        maxx=i[1]

maxappear=[]
for i in wordlst:
    if i[1]==maxx:
        maxappear.append(i[0])

if len(maxappear)!=1:
    print("?")
else:
    print(maxappear[0])
            pass
