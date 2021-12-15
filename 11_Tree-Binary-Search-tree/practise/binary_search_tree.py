class Node():
    def __init__(self, value=0):
        self.data = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def addNode(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            trav = self.root
            while(True):
                if new_node.data < trav.data:
                    if trav.left is None:
                        trav.left = new_node
                        break
                    trav = trav.left
                else: # new_node.data >= trav.data
                    if trav.right is None:
                        trav.right = new_node
                        break
                    trav = trav.right

    def _recurPreOrder(self, trav):
        if trav is None:
            return
        print(trav.data, ", ", end="")
        self._recurPreOrder(trav.left)
        self._recurPreOrder(trav.right)
    
    def recurPreOrder(self):
        print("PreOrder Traversal: ", end = "")
        self._recurPreOrder(self.root)
        print(" ")

    def _recurInOrder(self, trav):
        if trav is None:
            return
        self._recurInOrder(trav.left)
        print(trav.data, " ", end="")
        self._recurInOrder(trav.right)

    def recurInOrder(self):
        print("InOrder Traversal: ", end="")
        self._recurInOrder(self.root)
        print(" ")

    def _recurPostOrder(self, trav):
        if trav is None:
            return
        self._recurPostOrder(trav.left)
        self._recurPostOrder(trav.right)
        print(trav.data, " ", end="")

    def recurPostOrder(self):
        print("PostOrder Traversal: ", end="")
        self._recurPostOrder(self.root)
        print(" ")

if __name__=="__main__":
    bst = BinarySearchTree()
    bst.addNode(50)
    bst.addNode(30)
    bst.addNode(10)
    bst.addNode(70)
    bst.addNode(90)
    bst.addNode(40)
    bst.addNode(60)
    bst.addNode(20)
    bst.addNode(55)
    bst.addNode(65)
    bst.addNode(80)

    bst.recurPreOrder()
    bst.recurInOrder()
    bst.recurPostOrder()
