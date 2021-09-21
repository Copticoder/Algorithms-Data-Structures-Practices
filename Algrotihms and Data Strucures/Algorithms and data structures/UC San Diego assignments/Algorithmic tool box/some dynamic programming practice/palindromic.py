n= int(input())
listStr= input()
if '-' not in listStr:
    listStr=listStr.split(' ')
    for i in listStr:
        if i[::-1]==i:
            print (True)
            exit() 
    print(False)
else: print(False)
