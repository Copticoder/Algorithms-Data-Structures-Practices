n=int(input())
stack=[]
auxStack=[]
query=[]
maximum=0
while n:
    a,*b=input().split(' ')
    if a == 'max':
        query.append(maximum)
    elif a == 'pop':
        if stack[-1]==maximum:
            auxStack.pop(-1)
            maximum=auxStack[-1]
        stack.pop(-1)
    elif a == 'push':
        stack.append(int(*b))
        if int(*b) >= maximum:
            maximum=int(*b)
            auxStack.append(maximum)
    n-=1
for i in query:
    print(i)
