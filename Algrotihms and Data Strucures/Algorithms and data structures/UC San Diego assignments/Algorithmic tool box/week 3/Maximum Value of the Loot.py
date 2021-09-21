a,*b=input().split(' ')
weightsValsRatio=[]
weights=[]
i=0
while i<int(a):
    x,*y=input().split(' ')
    weightsValsRatio.append(int(x)/int(*y))
    weights.append(int(*y))
    i+=1
i=0
record=0
bagWeight=int(*b)
maxWeight=weightsValsRatio.index(max(weightsValsRatio))
while bagWeight > 0:
  if max(weights)!=0:  
    if weights[maxWeight]>0:
        record=record+(max(weightsValsRatio)*min(weights[maxWeight],bagWeight))
        bagWeight=bagWeight-min(weights[maxWeight],bagWeight)
        weights[maxWeight]=weights[maxWeight]-record
    else:
        weights[maxWeight]=0
        weightsValsRatio[maxWeight]=0
        maxWeight=weightsValsRatio.index(max(weightsValsRatio))
  else:
      break

print(('%.4f') %record)


