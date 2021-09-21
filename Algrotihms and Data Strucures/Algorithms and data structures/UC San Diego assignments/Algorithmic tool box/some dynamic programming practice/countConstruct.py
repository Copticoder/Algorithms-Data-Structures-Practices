from typing import Counter


memo={}
target='eeeeeeeeeeeeeeeeeeeef'
words=['e','ee','eee','eeee','eeeee']
def canConstruct(target,words,memo):
    if target in memo:
        return memo[target]
    if target=='':
        return True
    Counter=0
    for i in words:
        if target.find(i)==0:
            suffix=target[(len(i)):]
            result=canConstruct(suffix,words,memo)
            Counter+=result
            memo[target]=Counter
    return Counter
print(canConstruct(target,words,memo))
