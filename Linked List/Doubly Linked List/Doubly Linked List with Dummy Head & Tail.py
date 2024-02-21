# dummyHead = the node before the head node, dummyTail = the node after the tail node.
# Here head = self.dummyHead.next and tail = self.dummyTail.prev always. So we don't even need to keep track of head and tail.

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.dummyHead = Node(-1)
        self.dummyTail = Node(-1)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        temp = self.dummyHead.next # temp = head
        while index != 0:
            temp, index = temp.next, index - 1
        return temp.data

    def addAtHead(self, val: int) -> None:
        newNode, dummyHead, head = Node(val), self.dummyHead, self.dummyHead.next
        dummyHead.next = newNode
        newNode.next   = head
        newNode.prev   = dummyHead
        head.prev      = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode, dummyTail, tail = Node(val), self.dummyTail, self.dummyTail.prev
        tail.next      = newNode
        newNode.next   = dummyTail
        newNode.prev   = tail
        dummyTail.prev = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index >= self.size:
            self.addAtTail(val) if index  == self.size else None
            return

        newNode, nextNode = Node(val), self.dummyHead.next # temp = head
        while index != 0: # if index == 0, the loop won't even iterate
            nextNode, index = nextNode.next, index - 1
        prevNode = nextNode.prev

        prevNode.next = newNode
        newNode.next, newNode.prev = nextNode, prevNode
        nextNode.prev = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        
        nextNode = self.dummyHead.next # temp = head
        while index != 0: # if index == 0, the loop won't even iterate
            nextNode, index = nextNode.next, index - 1
        prevNode, nextNode = nextNode.prev, nextNode.next

        prevNode.next, nextNode.prev = nextNode, prevNode
        self.size -= 1

    def printFromFront(self) -> None:
        curNode = self.dummyHead.next # curNode = head
        while curNode.next:
            print(curNode.data, end=' -> ' if curNode.next.next else '')
            curNode = curNode.next
        print('\nSize =', self.size, '\n')

    def printFromBack(self) -> None:
        curNode = self.dummyTail.prev # curNode = tail
        while curNode.prev:
            print(curNode.data, end=' -> ' if curNode.prev.prev else '')
            curNode = curNode.prev
        print('\nSize =', self.size, '\n')
    
# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.printFromFront()
obj.printFromBack()
obj.deleteAtIndex(2)
obj.printFromFront()
obj.printFromBack()