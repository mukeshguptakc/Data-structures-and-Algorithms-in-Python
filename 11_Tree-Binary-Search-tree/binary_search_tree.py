
class Stack:
    def __init__(self):
        self.arr = list()
    
    def  push(self, val):
        self.arr.append(val)

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[len(self.arr)-1]
    
    def isEmpty(self):
        return len(self.arr) == 0

class Queue:
    def __init__(self):
        self.arr = list()

    def push(self, val):
        self.arr.append(val)
    
    def pop(self):
        return self.arr.pop(0)
    
    def peek(self, val):
        return self.arr[0]
    
    def isEmpty(self):
        return len(self.arr) == 0

class Node():
    def __init__(self, val=0):
        self.data = val
        self.left = None
        self.right = None

class BinSearchTree():
    def __init__(self):
        self.root = None

    def add(self, val):
        newNode = Node(val)
        if self.root is None :
            self.root = newNode
        else:
            trav = self.root
            while(True):
                if val < trav.data: # if less, goto left
                    if trav.left == None:
                        trav.left = newNode
                        break
                    trav = trav.left
                else: # else value more than trav, goto right
                    if trav.right == None:
                        trav.right = newNode
                        break
                    trav = trav.right
    
    def _recurPreOrder(self, trav):
        if (trav == None):
            return
        print(trav.data, ", ", end="")
        self._recurPreOrder(trav.left)
        self._recurPreOrder(trav.right)

    def recurPreOrder(self):
        print("PRE : ", end = "")
        self._recurPreOrder(self.root)
        print(" ")

    def _recurInOrder(self, trav):
        if (trav == None):
            return
        self._recurInOrder(trav.left)
        print(trav.data, ", ", end = "")
        self._recurInOrder(trav.right)

    def recurInOrder(self):
        print("In : ", end = "")
        self._recurInOrder(self.root)
        print(" ")

    def _recurPostOrder(self, trav):
        if (trav == None):
            return
        self._recurPostOrder(trav.left)
        self._recurPostOrder(trav.right)
        print(trav.data, ", ", end = "")
    
    def recurPostOrder(self):
        print("POST: ", end = "")
        self._recurPostOrder(self.root)
        print(" ")

    def findWithParent(self, val):
        pass
        

    def find(self, val):
        pass

    def depthFirstSearch(self):
        print("DFS: ", end="")
        s = Stack()
        s.push(self.root)
        while not s.isEmpty():
            trav = s.pop()
            print(trav.data, end=", ")
            if trav.right is not None:
                s.push(trav.right)
            if trav.left is not None:
                s.push(trav.left)
        print()

    def breadthFirstSearch(self):
        print("BFS: ", end="")
        q = Queue()
        q.push(self.root)
        while not q.isEmpty():
            trav = q.pop()
            print(trav.data, end=", ")
            if trav.left is not None:
                q.push(trav.left)
            if trav.right is not None:
                q.push(trav.right)
        print()

if __name__=="__main__":
    bst = BinSearchTree()
    bst.add(50)
    bst.add(30)
    bst.add(90)
    bst.add(10)
    bst.add(40)
    bst.add(70)
    bst.add(100)
    bst.add(20)
    bst.add(60)
    bst.add(80)
    bst.recurPreOrder()
    bst.recurInOrder()
    bst.recurPostOrder()
    bst.depthFirstSearch()
    bst.breadthFirstSearch()

"""
python binary_search_tree.py 
PRE : 50 , 30 , 10 , 20 , 40 , 90 , 70 , 60 , 80 , 100 ,  
In : 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100 ,  
POST: 20 , 10 , 40 , 30 , 60 , 80 , 70 , 100 , 90 , 50 ,  
DFS: 50, 30, 10, 20, 40, 90, 70, 60, 80, 100, 
BFS: 50, 30, 90, 10, 40, 70, 100, 20, 60, 80,
"""