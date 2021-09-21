n=int(input())
i=1
prizeList=[]
sumPrizes=sum(prizeList)
while sumPrizes<=n:
        prizeList.append(i)
        i+=1
        sumPrizes=sum(prizeList)

prizeList.remove(sumPrizes-n)
print(len(prizeList))
print(*prizeList)