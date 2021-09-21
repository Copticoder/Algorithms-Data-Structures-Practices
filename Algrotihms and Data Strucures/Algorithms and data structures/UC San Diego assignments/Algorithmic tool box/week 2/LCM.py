def LCM(x,y):
    funcVar=1
    xFunc=x*funcVar
    yFunc=y*funcVar
    if y>x:
        newVar= y-x
        while xFunc!=yFunc:
            xFunc=x*(funcVar+newVar)
            yFunc=y*funcVar
            funcVar+=1
        return xFunc
    else:
        newVar=x-y
        while xFunc!=yFunc:
            xFunc=x*funcVar
            yFunc=y*(funcVar+newVar)
            funcVar+=1
        return yFunc
   
    
    
print(LCM(15,12))