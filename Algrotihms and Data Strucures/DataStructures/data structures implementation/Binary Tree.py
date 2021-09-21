class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return BinaryTree.preorder_search(self,self.root,find_val)

    def print_tree(self):
        
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return BinaryTree.preorder_print(self,self.root,"")[:-1]
    def printHeight(self):
        return BinaryTree.heightTree(self,self.root)
    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True

            if BinaryTree.preorder_search(self,start.left,find_val) == True:
                return True
            if BinaryTree.preorder_search(self,start.right,find_val) == True:
                return True
        return False
    def heightTree(self,theNode):
        if theNode is None:
            return 0
        return 1+max(BinaryTree.heightTree(self,theNode.left),BinaryTree.heightTree(self,theNode.right))
    def preorder_print(self, start,traversal):
        if start:
            traversal+=(str(start.value)+'-')
            traversal=BinaryTree.preorder_print(self,start.left,traversal)
            traversal=BinaryTree.preorder_print(self,start.right,traversal)
        return traversal
        




 
# # Set up tree
# tree = BinaryTree(1)
# tree.root.left = Node(3)
# tree.root.right = Node(4)
# tree.root.right.left = Node(0)
# tree.root.right.right = Node(2)
# print(tree.printHeight())
# # Test search
# # Should be True
# print (tree.search(treeObj[1].value))
# # # Should be False
# print (tree.search(treeObj[2].value))

# # Test print_tree
# # Should be 1-2-4-5-3
# print(tree.print_tree())