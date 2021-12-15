
class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None
        self.prev = None

class DoublyListWithHead:
    def __init__(self):
        self.head = None
    
    # time complexity - O(1)
    def addFirst(self, val):
        newNode = Node(val)
        # Special case handling: if list is empty
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    # time complexity - O(n)
    def addLast(self, val):
        newNode = Node(val)
        # special case handling: if list is empty
        if self.head is None:
            self.head = newNode # newNode itself is first node of list and head.
        else:
            # traverse till last node 
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            # add address of newnode into last node's next
            trav.next = newNode
    
    # time complexity O(n)
    def displayForward(self):
        print("Forward List:", end=" ")
        trav = self.head
        while trav is not None:
            print(trav.data , end=", ")
            trav =  trav.next
        print()

    # time complexity O(n)
    def displayReverse(self):
        print("Reverse List:", end=" ")
        if self.head:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            while trav is not None:
                print(trav.data , end=", ")
                trav =  trav.prev
            print()


    # time complexity O(n)
    def addAtPosition(self, val, pos):
        #special 4. invalid pos(-1)
        if pos < 1:
            self.addFirst(val)
        #special 1. if list is empty OR special 2. add at Position = 1
        if self.head is None or pos == 1:
            self.addFirst(val)
        else:
            #create new node
            newNode = Node(val)
            #traverse till position - 1
            trav = self.head
            for _ in range(1, pos-1):
                trav = trav.next
                # Special 3. if Position is beyond the list length, 
                # then break and add at last position
                if trav.next is None:
                    break
            #add node at position
            newNode.next = trav.next
            trav = newNode

    # time complexity O(1)
    def delFirst(self):
        if self.head is None:
                print("List is Empty")
        self.head = self.head.next

    # time complexity O(n):
    def delAtPosition(self, pos):
        print("Delete at Position:",pos, end=" : ")
        # special 3: if pos < 1, return
        if pos < 1:
            print("Position less than 1")
            return
        # special 1: list is empty & 2: pos == 1
        if self.head is None or pos == 1:
            self.delFirst()
        else:
            trav = self.head
            for _ in range(1, pos-1):
                trav = trav.next
                # special 4: position > length of list return
                if trav.next is None:
                    print("Position Beyond List length:", pos)
                    return
            temp = trav.next
            # special 5: pos == length, if temp is null, Invalid Position.
            if temp is None:
                print("Invalid position:", pos)
                return
            trav.next = temp.next

    # time complexity - O(n)
    def delLast(self):
        # special 1: List is empty, Special 2: list has only one Node.
        if self.head is None or self.head.next is None:
            self.delFirst()
        else:
            prev = None
            trav = self.head
            while trav.next is not None:
                prev = trav
                trav = trav.next
            prev.next = None

    # time complexity O(n)
    def delAll(self):
        while self.head is not None:
            self.delFirst()
        #self.head = None  



if __name__=="__main__":
    L1 = DoublyListWithHead()
    L1.addLast(11)
    L1.addLast(22)
    L1.addLast(33)
    L1.addLast(44)
    L1.display()
    L1.addAtPosition(55, 2)
    L1.delFirst()
    L1.display()
    L1.delLast()
    L1.delAtPosition(3)
    L1.display()
