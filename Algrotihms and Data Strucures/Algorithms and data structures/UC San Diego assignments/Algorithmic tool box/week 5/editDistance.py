exString=str(input())
wantedString=str(input())
exWantedArray=[[] for val in range(len(wantedString)+1)]
for i in range(len(wantedString)+1):
    for j in range(len(exString)+1):
        exWantedArray[i].append(0)
def editDistance(exString,wantedString):
    for m in range(len(exString)+1):
            exWantedArray[0][m]=m
    for n in range(len(wantedString)+1):
        exWantedArray[n][0]=n
    for z in range(1,(len(wantedString)+1)):
        for x in range(1,(len(exString)+1)):
            if exString[x-1]!=wantedString[z-1]:
                exWantedArray[z][x]=min(exWantedArray[z-1][x],exWantedArray[z][x-1],exWantedArray[z-1][x-1])+1
            else:
                exWantedArray[z][x]=exWantedArray[z-1][x-1]
    return exWantedArray[-1][-1]
print(editDistance(exString,wantedString))