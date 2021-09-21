
n=int(input())
firstSeq=list(map(int, input().split()))
m=int(input())
secndSeq=list(map(int, input().split()))
if n<m:
    n, m = m, n
    secndSeq, firstSeq = firstSeq, secndSeq
sequenceArray=[[] for val in range(max(n,m)+1)]
for i in range(n+1):
    for _ in range(m+1):
        sequenceArray[i].append(0)
def lcs(firstSec,secndSeq):
    for l in range(1,len(firstSeq)+1):
        for m in range(1,len(secndSeq)+1):
            if firstSeq[l-1]==secndSeq[m-1]:
                sequenceArray[l][m]=1+sequenceArray[l-1][m-1]
            else:
                sequenceArray[l][m]=max(sequenceArray[l-1][m],sequenceArray[l][m-1])
    # if sequenceArray[-1][-1]:
    return sequenceArray[-1][-1]
    # else:
        # return 0

print(lcs(firstSeq,secndSeq))
