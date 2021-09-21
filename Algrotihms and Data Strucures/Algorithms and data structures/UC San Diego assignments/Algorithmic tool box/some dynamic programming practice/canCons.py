string='abcdef'
stringArr=['ab','def','abc','abcd','abc','cd']
def canConstruct(wantedString,stringArra):
    newArr=[False]*(len(wantedString)+1)
    newArr[0]=True
    modifiedString=wantedString
    for i in range(len(newArr)):
        for j in stringArr:
            if newArr[i] !=False:
                if modifiedString.find(j)==0:
                    if i+len(j)<len(newArr):
                        newArr[i+len(j)]=True
            else:
                continue
        modifiedString=wantedString[(i+1):]
    return newArr
print(canConstruct(string,stringArr))