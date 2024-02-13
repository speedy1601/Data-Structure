from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, headValue=None):
        self.head = Node(headValue) if headValue != None else None
    
    def __init__(self, Nodes: list):
        self.head = Node(Nodes[0])
        prevNode = self.head

        for i in range(1, len(Nodes)):
            curNode = Node(Nodes[i])
            prevNode.next = curNode
            prevNode = curNode

    def addEnd(self, value) -> None:
        newNode, temp = Node(value), self.head
        if self.head == None:
            self.head = newNode
        else:
            while temp.next != None: # stop on the Last Node
                temp = temp.next
            temp.next = newNode
    
    def addFront(self, value) -> None:
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    
    def deleteNode(self, target) -> str:
        curNode, prevNode = self.head, None
        while curNode != None:
            if curNode.data == target:
                if prevNode == None: # if curNode == self.head
                    self.head = self.head.next
                else:
                    prevNode.next = curNode.next
                return "Successfully deleted!"
            prevNode = curNode
            curNode = curNode.next

        return f"{target} not found!"

    def printList(self) -> None:
        temp = self.head
        while temp != None:
            print(temp.data, '-> ' if temp.next != None else '', end='')
            temp = temp.next
        print()

    def printList1(self, headNode: Node) -> None:
        temp = headNode
        while temp != None:
            print(temp.data, '-> ' if temp.next != None else '', end='')
            temp = temp.next
        print()
    
    def printReverse(self, headNode) -> None:
        if headNode.next == None:
            print(headNode.data, end='')
            return
        self.printReverse(headNode.next)
        print(' -> ', end='')
        print(headNode.data, end='')
    
    def reverseList(self, headNode) -> Node: # https://leetcode.com/problems/reverse-linked-list/description/
        curNode, prevNode = headNode, None
        while curNode != None:
            nextLink = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextLink
        
        return prevNode
    
    def reverseBetween(self, headNode: Node, left: int, right: int) -> Node: # https://leetcode.com/problems/reverse-linked-list-ii/
        prevLeftNode, curNode, prevNode = None, headNode, None
        for _ in range(1, left):
            prevLeftNode, curNode = curNode, curNode.next
        leftNode = curNode
        
        for _ in range(left, right+1):
            nextLink = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextLink
        
        if prevLeftNode != None:
            prevLeftNode.next = prevNode
        leftNode.next = curNode
        return prevNode if left == 1 else headNode
    
    def removeElements(self, headNode: Node, val: int) -> Node: # https://leetcode.com/problems/remove-linked-list-elements/description/
        dummyHead = Node(-1)
        dummyHead.next = headNode
        curNode, prevNode = headNode, dummyHead
        while curNode != None:
            if curNode.data == val:
                prevNode.next = curNode.next
            else:
                prevNode = curNode
            curNode = curNode.next
        
        return dummyHead.next
    
    def deleteDuplicates(self, headNode: Node) -> Node: # https://leetcode.com/problems/remove-duplicates-from-sorted-list/
        curNode = headNode
        while curNode != None and curNode.next != None:
            if curNode.data == curNode.next.data:
                while curNode.next != None and curNode.next.data == curNode.data:
                    curNode.next = curNode.next.next
            curNode = curNode.next

        return headNode
    
    def deleteDuplicatesii(self, headNode: Node) -> Node: # https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
        dummyHead = Node(-1)
        dummyHead.next = headNode
        curNode, prevNode = headNode, dummyHead

        while curNode != None and curNode.next != None:
            if curNode.data == curNode.next.data:
                while curNode.next != None and curNode.next.data == curNode.data:
                    curNode.next = curNode.next.next
                prevNode.next = curNode.next
            else:
                prevNode = curNode
            curNode = curNode.next
        
        return dummyHead.next
    
    def removeNodes(self, headNode: Node) -> Node: # https://leetcode.com/problems/remove-nodes-from-linked-list/
        dummyHead, curNode = Node(float('inf')), headNode
        stack = deque([dummyHead])
        
        while curNode != None:
            while stack and curNode.data > stack[-1].data:
                stack.pop()
            stack[-1].next = curNode
            stack.append(curNode)
            curNode = curNode.next
        
        return dummyHead.next
    
    def middleNode(self, headNode: Node) -> Node: # https://leetcode.com/problems/middle-of-the-linked-list/description/
        slow = fast = headNode
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def middleNode1(self, headNode: Node) -> Node: # here for even nodes like for for 4 nodes, 2nd one is Middle which is opposite
        slow = fast = headNode                     # of the above middleNode(..) method.
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(fast.data if fast else None)
        return slow
    
    def deleteMiddle(self, headNode: Node) -> Node: # https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
        dummyHead = Node(-1)
        dummyHead.next = headNode
        slow, fast, prevNode = headNode, headNode, dummyHead

        while fast and fast.next:
            prevNode = slow
            slow = slow.next
            fast = fast.next.next
        
        prevNode.next = slow.next
        return dummyHead.next

    def oddEvenList(self, headNode: Node) -> Node: # https://leetcode.com/problems/odd-even-linked-list/description/
        if headNode == None:
            return headNode
        odd, even, evenHead = headNode, headNode.next, headNode.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        return headNode
    
    def swapNodes(self, headNode: Node, k: int) -> Node: # https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
        first = last = headNode
        for _ in range(k-1):
            first = first.next
        first1 = first

        while first1.next:
            last = last.next
            first1 = first1.next
        
        first.data, last.data = last.data, first.data
        return headNode
    
    def rotateRight(self, headNode: Node, k: int) -> Node: # https://leetcode.com/problems/rotate-list/description/
        if headNode == None:
            return headNode
        last, prevOfFirst, length = headNode, headNode, 1

        while last.next:
            length += 1
            last = last.next
        k = k % length
        if k == 0: return headNode

        for _ in range(length - k - 1):
            prevOfFirst = prevOfFirst.next
        first = prevOfFirst.next

        prevOfFirst.next = None
        last.next = headNode
        return first
    
    def mergeInBetween(self, list1: Node, a: int, b: int, list2: Node) -> Node: # https://leetcode.com/problems/merge-in-between-linked-lists/
        first, last, list2Tail = None, list1, list2

        while list2Tail.next:
            list2Tail = list2Tail.next
        
        for i in range(b+1):
            if i == a-1:
                first = last
            last = last.next
        
        first.next = list2
        list2Tail.next = last
        return list1

    def reverseAndLength(self, headNode: Node) -> tuple:
        temp, prevNode, length = headNode, None, 0

        while temp:
            curNode = Node(temp.data)
            curNode.next = prevNode
            prevNode = curNode
            temp = temp.next
            length += 1

        return (prevNode, length)
    
    def reorderList(self, head: Node) -> None: # https://leetcode.com/problems/reorder-list/description/
        # seprating 2 lists into list1 and list2
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        list2, slow.next = slow.next, None

        # reversing list2
        curNode, prevNode = list2, None
        while curNode:
            next = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = next
        
        # linking
        list1, list2, prevNode = head, prevNode, Node(-1)
        while list2:
            next1 = list1.next
            list1.next = list2
            prevNode.next = list1
            prevNode = list2
            list1, list2 = next1, list2.next
        
        prevNode.next = list1 if list1 else None
    
    def isPalindrome(self, head: Node) -> bool: # https://leetcode.com/problems/palindrome-linked-list/
        # seprating 2 lists into list1 and list2
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        list2, slow.next = slow.next, None

        # reversing list2
        curNode, prevNode = list2, None
        while curNode:
            next = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = next
        
        # comparing
        list1, list2 = head, prevNode
        while list2:
            if list1.data != list2.data:
                return False
            list1, list2 = list1.next, list2.next
        return True
        

    def mergeTwoLists(self, list1: Node, list2: Node) -> Node: # https://leetcode.com/problems/merge-two-sorted-lists/description/
        dummyHead = Node(-1)
        first, second, prevMinNode = list1, list2, dummyHead

        while first and second:
            minNode = first if first.data < second.data else second
            prevMinNode.next = minNode
            prevMinNode = minNode
            if minNode == first:
                first = first.next
            else:
                second = second.next
        
        restNodes = first if first else second
        prevMinNode.next = restNodes
        return dummyHead.next
    
    def hasCycle(self, headNode: Node) -> bool: # https://leetcode.com/problems/linked-list-cycle/
        slow = fast = headNode
         
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return True
        
        return False

def main():
    sll = SinglyLinkedList([1])
    sll.printList()
    print(sll.isPalindrome(sll.head))

if __name__ == '__main__':
    main()