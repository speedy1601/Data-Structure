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


def main() -> None:
    T = BST()
    for v in [8, 3, 1, 6, 10, 14, 13]:
        T.insert1(v)
    T.printLevelByLevel()

    print(T.getMinimumDifference(T.root))

if __name__ == '__main__':
    main()