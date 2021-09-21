n=int(input())
listString=input().split(' ')
x=0
salaryList=[]
for i in listString:
  if i == ' ':
    listString.remove(i)
print(listString)
while len(listString)>0:
  maxNum=-1    
  for z in listString:
    if int(z)>9:
      if int(z)/10>=maxNum:
        maxNum=int(z)/10
        ratioHolder=int(z)
    else:
      if int(z)>=maxNum:
        maxNum=int(z)
        ratioHolder=int(z)       
  
  salaryList.append(str(ratioHolder))
  listString.remove(str(ratioHolder))
  


for p in salaryList:
    print(p,end='')

#23 22 11 2 2 40 4 