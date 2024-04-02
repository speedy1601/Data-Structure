from collections import deque
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
    
    def printLevelByLevel(self) -> None:
        q = deque([self.root] if self.root else [])
        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                print(curNode.val, end=' ')
                if curNode.left:  q.append(curNode.left)
                if curNode.right: q.append(curNode.right)
            print()
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode: # https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
        if root == None:
            return TreeNode(val)
        if val < root.val:
            root.left  = self.insertIntoBST(root.left,  val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

def main() -> None:
    T = BST()
    for v in [8, 3, 10, 1, 6, 14]:
        T.insert1(v)
    T.printLevelByLevel()

if __name__ == '__main__':
    main()