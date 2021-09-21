class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1


def insert(node, root):
    p = find(root, node.value)
    if p.value < node.value:
        p.right = node
    else:
        p.left = node

    node.parent = p


def find(root, key):
    if root.value == key:
        return root
    elif root.value < key:
        if root.right:
            return find(root.right, key)
        return root
    elif root.value > key:
        if root.left:
            return find(root.left, key)
        return root


def delete(node):
    if node.right:
        nxtNode = next(node)
        node.value = nxtNode.value
        if nxtNode.right:
            nxtNode = nxtNode.right
    elif node.left:
        node = node.left
    elif node.parent.value < node.value:
        node.parent.right = None
    else:
        node.parent.left = None


def next(node):
    if node.right:
        return leftDescendant(node.right)
    return rightAncestor(node)


def rangeSearch(x, y, root):
    listNodes = []
    p = find(root, x)
    while p.value <= y:
        if p.value >= x:
            listNodes.append(p.value)
        p = next(p)
    return listNodes


def leftDescendant(node):
    if node.left:
        return leftDescendant(node.left)
    return node


def rightAncestor(node):
    if node:
        if node.parent and node.value < node.parent.value:
            return node.parent
        return rightAncestor(node.parent)
    return None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

r = Node(50)
n1 = Node(30)
n2 = Node(20)
n3 = Node(40)
n4 = Node(70)
n5 = Node(60)
n6 = Node(80)
insert(n1, r)
insert(n2, r)
insert(n3, r)
insert(n4, r)
insert(n5, r)
insert(n6, r)
delete(n5)
inorder(r)
print(*rangeSearch(20, 50, r))
print(find(r, 30).value)
print(next(n5).value)

#       50
#     30   70
#   20 40 60 80
