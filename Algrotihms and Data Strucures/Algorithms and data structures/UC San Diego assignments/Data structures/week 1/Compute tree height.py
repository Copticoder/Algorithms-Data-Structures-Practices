class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Set up tree
n=int(input())
parentList=list(map(int, input().split()))
treeObj = [Node(i) for i in range(n)]
for z, j in enumerate(parentList):
    if j==-1:
        treeHead=treeObj[z]
    elif treeObj[j].left:
        treeObj[j].right=treeObj[z]
    else:
        treeObj[j].left=treeObj[z]
def heightTree(theNode):
    if theNode is None:
        return 0
    return 1+max(heightTree(theNode.left),heightTree(theNode.right))

print(heightTree(treeHead))
