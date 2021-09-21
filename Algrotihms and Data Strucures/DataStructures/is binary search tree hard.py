import sys
import threading

sys.setrecursionlimit(10**8)  # max depth of recursion
threading.stack_size(2**27)

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


n = int(input())
finalList = []
vrtcs = []
nodes = []


def getInput(n):
    while n:
        vrt = list(map(int, input().split(' ')))
        vrtcs.append(vrt)
        n -= 1


def appendNodes():
    for j in range(len(vrtcs)):
        nodes.append(Node(vrtcs[j][0]))
    for i in range(len(vrtcs)):
        if vrtcs[i][1] != -1:
            nodes[i].left = nodes[vrtcs[i][1]]
        if vrtcs[i][2] != -1:
            nodes[i].right = nodes[vrtcs[i][2]]

# def isBST(node,min,max):
#     if node:
#         if node.key<min or node.key>=max:
#             return False
#         return isBST(node.left,min,node.key) and isBST(node.right,node.key,2147483647)
#     return True
def isOnLeft(key, left):
    if left !=None:
        return left.key < key
    return True

def isOnRight(key, right):
    if right !=None:
        return right.key >= key
    return True
def isBST(root):
    if root != None:
        return isOnLeft(root.key, root.left) and isOnRight(root.key, root.right) and isBST(root.left) and isBST(root.right)
    return True




def main():
    if n:
        getInput(n)
        appendNodes()
        root = nodes[0]
        if isBST(root):
            print("CORRECT")
        else:
            print("INCORRECT")

    else:
        print('CORRECT')


threading.Thread(target=main).start()
