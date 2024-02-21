# https://leetcode.com/problems/design-linked-list/description/
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curNode = self.head
        while index != 0:
            curNode, index = curNode.next, index - 1
        return curNode.data

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head # head may exist or not doesn't matter.
        if self.head: self.head.prev = newNode
        self.head = newNode
        if self.head.next == None: self.tail = self.head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.addAtHead(val)
        else:
            newNode = Node(val)
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            newNode, nextNode = Node(val), self.head
            while index != 0:
                nextNode, index = nextNode.next, index - 1
            prevNode = nextNode.prev

            prevNode.next = newNode
            newNode.prev  = prevNode
            newNode.next  = nextNode
            nextNode.prev = newNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        dummyHead = Node(-1)
        dummyHead.next, self.head.prev = self.head, dummyHead # linking dummyHead and head
        curNode, idx = self.head, index

        while index != 0:
            curNode, index = curNode.next, index - 1
        curNode.prev.next = curNode.next
        if curNode.next: curNode.next.prev = curNode.prev

        if dummyHead.next: dummyHead.next.prev = None # removing the linking of dummyHead and head
        self.head = dummyHead.next
        if idx == self.size-1: self.tail = self.tail.prev # if index pointing the tail node, new tail = tail.prev
        self.size -= 1
        
    def printList(self):
        curNode = self.head
        while curNode:
            print(curNode.data, end=' -> ' if curNode.next != None else '')
            curNode = curNode.next
        print(f" (Size = {self.size})")
    
    def printList1(self):
        curNode = self.tail
        while curNode:
            print(curNode.data, end=' -> ' if curNode.prev != None else '')
            curNode = curNode.prev
        print(f" (Size = {self.size})")

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
#param_1 = obj.get(index)b  
obj.addAtHead(1)
obj.printList()
obj.addAtTail(2)
obj.printList()
obj.addAtIndex(0,3)
obj.printList()
print(obj.get(2))
obj.deleteAtIndex(0)
obj.printList()