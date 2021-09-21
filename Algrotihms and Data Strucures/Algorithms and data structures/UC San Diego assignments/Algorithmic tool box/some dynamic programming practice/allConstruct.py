memo={}
target='word'
words=['or','wo','d','r','w']
def canConstruct(target,words,memo={}):
    # if target in memo:
    #     return memo[target]
    if target=='':
        return [[]]
    resultArr=[]
    for i in words:
        if target.find(i)==0:
            suffix=target[(len(i)):]
            result=canConstruct(suffix,words,memo)
                # memo[target]=True
            newAll=[*result,i]
            resultArr.insert(-1,newAll)
    # memo[target]=False
    return resultArr
print(canConstruct(target,words,memo))
