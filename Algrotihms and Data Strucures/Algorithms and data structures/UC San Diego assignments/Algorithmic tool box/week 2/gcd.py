# def gcd(a,b):
#     if b == 0:
#         return a
#     else:
#         c=a%b
#         return gcd(b,c)
# a,*b=input().split()
# print(gcd(int(a),int(*b)))
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm
a,*b=input().split()
print(compute_lcm(int(a),int(*b)))