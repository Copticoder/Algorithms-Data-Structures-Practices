memo={}
coins=[1,2,5,25]
money=100
def change(money,coins,memo={}):
    if money in memo:
        return memo[money]
    if money == 0:
        return []
    if money<0:
        return None
    newComp=None    
    for i in coins:
        result=change(money-i,coins,memo)
        if result != None:
            resultComb=[*result,i]
            if newComp==None or len(newComp)>len(resultComb):
                newComp=resultComb
    memo[money]=newComp
    return newComp
print(change(money,coins,memo))    