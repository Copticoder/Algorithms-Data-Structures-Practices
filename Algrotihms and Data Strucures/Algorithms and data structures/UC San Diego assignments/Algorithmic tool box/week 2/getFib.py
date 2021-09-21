###MY####
# first=0
# scnd=1
# counter=0
# nextElement=0
# def get_fib(position):
#     global first,scnd,nextElement,counter
#     if position <=1:
#         return position
#     else:
#         first,scnd = scnd, nextElement
#         nextElement=first+scnd
#         counter+=1
#         if counter <position:
#             return get_fib(position)
#         else:
#             return nextElement    

###SECOND###

def fibbo(n):
    frst =0
    scnd=1
    nextNum=frst+scnd
    if n>=2:
        for i in range(2,n):
            frst=scnd
            scnd=nextNum
            nextNum=(frst+scnd)%10
        return nextNum
    elif n==0:
        return 0
    else:
        return 1
x=int(input())
print(fibbo(x))
# def fib(n):
 
#     # The first two Fibonacci numbers
#     f0 = 0
#     f1 = 1
 
#     # Base case
#     if (n == 0):
#         return 0
#     if (n == 1):
#         return 1
#     else:
 
#         # Pisano Period for % 10 is 60
#         rem = n % 60
 
#         # Checking the remainder
#         if(rem == 0):
#             return 0
 
#         # The loop will range from 2 to
#         # two terms after the remainder
#         for i in range(2, rem + 3):
#             f =(f0 + f1)% 60
#             f0 = f1
#             f1 = f
 
#         s = f1-1
#         return(s)
 
# # Driver code
# if __name__ == '__main__':
     
#     m = 10087887
#     n = 2983097899
 
#     final = fib(n)-fib(m-1)
 
#     print(final % 10)