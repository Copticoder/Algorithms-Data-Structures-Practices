import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27) 

class Node():
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.key,end=' ')
        inOrder(root.right)
def preOrder(root):
    if root:
        print(root.key,end=' ')
        preOrder(root.left)
        preOrder(root.right)
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.key,end=' ')
n=int(input())
vrtcs=[]
while n:
    vrt=list(map(int,input().split(' ')))
    vrtcs.append(vrt)
    n-=1
root=Node(vrtcs[0][0])
nodes=[]
for j in range(len(vrtcs)):
    nodes.append(Node(vrtcs[j][0]))
for i in range(len(vrtcs)):
    if vrtcs[i][1] !=-1:
        nodes[i].left=nodes[vrtcs[i][1]]
    if vrtcs[i][2] !=-1:
        nodes[i].right=nodes[vrtcs[i][2]]
def main():
    inOrder(nodes[0])
    print('')
    preOrder(nodes[0])
    print('')
    postOrder(nodes[0])

threading.Thread(target=main).start()

