class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        # Special 1: if list is empty. Special 4. Invalid index(-1). 
        if  self.head is None or index < 0:
            return 0
        # special 2. Index at = 0
        if index == 0:
            return self.head.data

        trav = self.head
        for _ in range(0, index):
            trav = trav.next
            # Special case 3. If Index is beyond the list length, 
            # then break and return index not found.
            if trav.next is None:
                return 0
        print("get: ", trav.data)
        return trav.data

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        #special case handling if list is empty
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        # Special case handling: if list is Empty
        if self.head == None:
            self.head = newNode # newNode itself is first and last node.
        else:
            # Traverse till last node
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            # add address of newnode into last node's next
            trav.next = newNode
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # Special case Invalid index
        if index < 0:
            return
        # Special 1. if list is empty or special 2. add at index = 0.
        if self.head is None or index == 0:
            self.addAtHead(val)
        else:
            #create new Node
            newNode = Node(val)
            # traverse till index - 1
            trav = self.head
            for _ in range(0, index-1):
                trav =  trav.next
                # Special 3. if index is beyond the list length,
                # then break and return
                if trav.next is None:
                    return
            #add node at position
            newNode.next = trav.next
            trav.next = newNode

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        # Special 3: if index < 0. return
        if index < 0:
            return
        # Special 1: list is empty & 2: index = 0
        if self.head is None or index == 0:
            self.head = self.head.next
        else:
            trav = self.head
            for _ in range(0, index):
                trav =  trav.next
                print("trav: ", trav.data)
            print("trav data at index:", trav.data)
            temp = trav.next
            trav.next = temp.next

    def display(self):
        print("List:", end=" ")
        trav = self.head
        while trav is not None:
            print(trav.data , end=", ")
            trav =  trav.next
        print()
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.display()
myLinkedList.addAtTail(3)
myLinkedList.display()
myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
myLinkedList.display()
myLinkedList.get(1)              # return 2
myLinkedList.display()
myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
myLinkedList.display()
myLinkedList.get(1)              # return 
myLinkedList.display()

# param_1 = 2
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

