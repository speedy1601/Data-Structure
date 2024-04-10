from collections import deque, defaultdict
from typing import List
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val) -> None: # recursion (O(n) space)
        if self.root == None:
            self.root = TreeNode(val)
            return
        
        def append(root: TreeNode) -> None:
            if val < root.val:
                if root.left == None:
                    root.left = TreeNode(val); return
                append(root.left)
            else:
                if root.right == None:
                    root.right = TreeNode(val); return
                append(root.right)
        
        append(self.root)
        # Also look at https://www.geeksforgeeks.org/insertion-in-binary-search-tree/
    
    def insert1(self, val) -> None: # iterative (O(1) space)
        if self.root == None:
            self.root = TreeNode(val)
            return
        
        cur, prev, addToLeft = self.root, None, True
        while cur:
            prev = cur
            addToLeft = val < cur.val
            cur = cur.left if val < cur.val else cur.right
        
        if addToLeft: prev.left  = TreeNode(val)
        else:         prev.right = TreeNode(val)
    
    def printLevelByLevel(self, root = None) -> None:
        q = deque([root] if root else [self.root] if self.root else [])
        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                if curNode == None:
                    print('null', end=' ')
                    continue
                print(curNode.val, end=' ')
                q.append(curNode.left)
                q.append(curNode.right)
            print()
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode: # https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
        if root == None:
            return TreeNode(val)
        
        cur, prev = root, None
        while cur:
            prev = cur
            cur = cur.left if val < cur.val else cur.right
        
        if val < prev.val: prev.left  = TreeNode(val)
        else:              prev.right = TreeNode(val)
        return root
    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode: # https://leetcode.com/problems/search-in-a-binary-search-tree/description/
        cur = root
        while cur and cur.val != val:
            cur = cur.left if val < cur.val else cur.right
        return cur
    
    def findMode(self, root: TreeNode) -> List[int]: # https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
        count, maxCount = defaultdict(lambda: 0), 0

        def traverse(Root: TreeNode) -> None:
            nonlocal maxCount
            if Root == None: return
            count[Root.val] += 1
            maxCount = max(maxCount, count[Root.val])
            traverse(Root.left); traverse(Root.right)
        
        traverse(root)
        return [ k for k, v in count.items() if v == maxCount ]
    
    def getMinimumDifference(self, root: TreeNode) -> int: # https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
        stack, curNode, prevNode, minDiff = [], root, None, float('inf')

        while curNode or stack:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            curNode = stack.pop()

            if prevNode != None:
                minDiff = min(minDiff, curNode.val - prevNode.val)
            prevNode = curNode

            curNode = curNode.right
        
        return minDiff
    
    def minDiffInBST(self, root: TreeNode) -> int: # https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
        stack, curNode, prevNode, minDiff = [], root, None, float('inf')

        while curNode or stack:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            curNode = stack.pop()

            if prevNode != None:
                minDiff = min(minDiff, curNode.val - prevNode.val)
            prevNode = curNode

            curNode = curNode.right

        return minDiff

    def increasingBST(self, root: TreeNode) -> TreeNode: # https://leetcode.com/problems/increasing-order-search-tree/description/
        dummyHead = prevNode = TreeNode(-1)

        def inorderTraverse(curNode: TreeNode) -> None:
            nonlocal prevNode
            if curNode == None:
                return
            inorderTraverse(curNode.left)
            prevNode.right = curNode
            curNode.left = None
            prevNode = curNode
            inorderTraverse(curNode.right)
        
        inorderTraverse(root)
        return dummyHead.right
    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int: # https://leetcode.com/problems/range-sum-of-bst/
        q, total = deque([root] if root else []), 0

        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                total  += curNode.val if low <= curNode.val <= high else 0
                if low  < curNode.val and curNode.left:
                    q.append(curNode.left)
                if high > curNode.val and curNode.right:
                    q.append(curNode.right)
        
        return total
    
    def binarySearch(self, root: TreeNode, target: int) -> bool:
        while root: # root passed as copy, so original root won't get modified
            if root.val == target:
                return True
            root = root.left if target < root.val else root.right
        return False

    def findTarget(self, root: TreeNode, k: int) -> bool: # https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
        q = deque([root] if root else [])
        
        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                target  = k - curNode.val
                if target != curNode.val and self.binarySearch(root, target) == True:
                    return True
                if curNode.left:  q.append(curNode.left)
                if curNode.right: q.append(curNode.right)
        
        return False
    
    def isValidBST(self, root: TreeNode) -> bool: # https://leetcode.com/problems/validate-binary-search-tree/description/
        stack, curNode, prev_value = [], root, None

        while curNode or stack:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            curNode = stack.pop()
            
            if prev_value != None and curNode.val <= prev_value:
                return False
            prev_value = curNode.val

            curNode = curNode.right
        
        return True
    
    def recoverTree(self, root: TreeNode) -> None: # https://leetcode.com/problems/recover-binary-search-tree/description/
        prevNode = first = middle = second = None

        def inorderTraverse(curNode: TreeNode) -> None:
            nonlocal prevNode, first, middle, second
            if curNode == None or second: # no more recursion after second found
                return
            
            inorderTraverse(curNode.left)
            if prevNode != None and curNode.val < prevNode.val:
                if first == None:
                    first, middle = prevNode, curNode
                else:
                    second = curNode
            prevNode = curNode
            inorderTraverse(curNode.right)
        
        inorderTraverse(root)
        if second == None:
            first.val, middle.val = middle.val, first.val
        else:
            first.val, second.val = second.val, first.val

def main() -> None:
    T = BST()
    for v in [32,26,47,19,56,27]:
        T.insert1(v)
    print(T.isValidBST(T.root))

if __name__ == '__main__':
    main()