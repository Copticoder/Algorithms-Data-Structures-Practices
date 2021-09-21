string='purple'
stringArr=['p','purp','ur','le','purpl']
def canConstruct(wantedString,stringArra):
    newArr=[[] for _ in range(len(wantedString) + 1)]
    newArr[0]=[[]]
    modifiedString=wantedString
    for i in range(len(newArr)):
        for j in stringArr:
                if modifiedString.find(j)==0:
                    if i+len(j)<len(newArr):
                       newCombination=[combination + [j] for combination in newArr[i]]
                       newArr[i+len(j)].extend(newCombination)
                else:
                 continue
        modifiedString=wantedString[(i+1):]
    return newArr
print(canConstruct(string,stringArr))