import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
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


def traverseInOrder(node):
    if node:
        traverseInOrder(node.left)
        finalList.append(node)
        traverseInOrder(node.right)


def checkList(finalList):
    for z in range(1, len(finalList)):
        if finalList[z].key <= finalList[z-1].key:
            return "INCORRECT"
    return 'CORRECT'

def main():
    if n:
        getInput(n)
        appendNodes()
        root = nodes[0]
        traverseInOrder(root)
        print(checkList(finalList))
    else:
        print("CORRECT")
threading.Thread(target=main).start()
