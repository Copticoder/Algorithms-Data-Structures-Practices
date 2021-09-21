memo={}
target='gay'
words=['or','wo','d','r','w']
def canConstruct(target,words,memo={}):
    if target in memo:
        return memo[target]
    if target=='':
        return True
    for i in words:
        if target.find(i)==0:
            suffix=target[(len(i)):]
            result=canConstruct(suffix,words,memo)
            if result==1:
                memo[target]=True
                return True
    memo[target]=False
    return False
print(canConstruct(target,words,memo))
