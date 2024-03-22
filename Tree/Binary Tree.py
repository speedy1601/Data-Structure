from collections import deque
import time
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.queue = deque() # it'll act like queue
    
    def insert(self, value) -> None:
        newNode = TreeNode(value)
        if self.root == None:
            self.root = newNode
            self.queue.append(newNode)
        else:
            appendNode = self.queue[0]
            if appendNode.left == None:
                appendNode.left = newNode
            else:
                appendNode.right = newNode
            self.queue.append(newNode)
            if appendNode.right != None: # appendNode's both left and right have node
                self.queue.popleft()
    
    def printLevelByLevel(self) -> None:
        if self.root == None:
            print('There is no node in the tree')
            return
        
        q = deque([self.root])
        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                print(curNode.val, end=' ')
                if curNode.left:  q.append(curNode.left)
                if curNode.right: q.append(curNode.right)
            print()
    
    def print_preOrder(self, root) -> None:
        if root == None:
            return
        print(root.val, end=' ')
        self.print_preOrder(root.left)
        self.print_preOrder(root.right)
    
    def preorderTraversal(self, root: TreeNode) -> list[int]: # https://leetcode.com/problems/binary-tree-preorder-traversal/
        stack, preorderList = [], []
        curNode = root

        while curNode or stack:
            while curNode:
                stack.append(curNode)
                preorderList.append(curNode.val)
                curNode = curNode.left
            curNode = stack.pop().right
        
        return preorderList

        # stack, preorderList = [root] if root else [], []

        # while stack:
        #     curNode = stack.pop()
        #     preorderList.append(curNode.val)
        #     if curNode.right:
        #         stack.append(curNode.right)
        #     if curNode.left:
        #         stack.append(curNode.left)
        
        # return preorderList

    def print_inOrder(self, root) -> None:
        if root == None:
            return
        self.print_inOrder(root.left)
        print(root.val, end=' ')
        self.print_inOrder(root.right)
    
    def inorderTraversal(self, root: TreeNode) -> list[int]: # https://leetcode.com/problems/binary-tree-inorder-traversal/description/
        stack, inorderList = [], []
        curNode = root

        while curNode or stack:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            curNode = stack.pop()
            inorderList.append(curNode.val)
            curNode = curNode.right
        
        return inorderList
    
    def print_postOrder(self, root) -> None:
        if root == None:
            return
        self.print_postOrder(root.left)
        self.print_postOrder(root.right)
        print(root.val, end=' ')

    def postorderTraversal(self, root: TreeNode) -> list[int]: # https://leetcode.com/problems/binary-tree-postorder-traversal/description/
        stack, postOrderList, visited = [], [], {None}
        curNode = root

        while curNode or stack:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            
            curNode = stack[-1]
            while curNode and (curNode.left in visited and curNode.right in visited):
                postOrderList.append(stack.pop().val) # stack.pop() == curNode
                visited.add(curNode)
                curNode = stack[-1] if stack else None
            curNode = stack[-1].right if stack else None
           
        return postOrderList
    
    def tree_max(self) -> int:
        def max_value_of(root) -> int: # similar to preOrder traversal where root process first, then root.left and root.right
            if root == None:
                return float('-inf')
            return max(root.val, max_value_of(root.left), max_value_of(root.right))
        return max_value_of(self.root)
    
    def tree_height(self) -> int: # distance from the Farthest Node to Root Node e.g. 4 -> 3, Distance from 3 to 4 is 1
        def heightOf(root) -> int:
            if root == None:
                return -1
            return max(heightOf(root.left), heightOf(root.right)) + 1
        return heightOf(self.root)

    def total_nodes(self) -> int:
        def total_nodes_from(root) -> int:
            if root == None:
                return 0
            return 1 + total_nodes_from(root.left) + total_nodes_from(root.right)
        return total_nodes_from(self.root)
        
        # if the Tree is Complete Binary Tree
        # return self.countNodes(root)
    
    def total_leaf_nodes(self) -> int:
        def total_leaf_nodes_of_the_tree(root) -> int:
            if root == None:
                return 0
            return (root.left == None and root.right == None) + total_leaf_nodes_of_the_tree(root.left) + total_leaf_nodes_of_the_tree(root.right)
        return total_leaf_nodes_of_the_tree(self.root)
    
    def is_exist(self, value) -> bool:
        def search_from(root) -> bool:
            if root == None:
                return False
            return any((root.val == value, search_from(root.left), search_from(root.right)))
        return search_from(self.root)
    
    def heights_and_total_nodes(self) -> tuple:
        node = 0
        def heightOf(root) -> int:
            if root == None:
                return -1
            nonlocal node; node += 1
            return max(1 + heightOf(root.left), 1 + heightOf(root.right))
        return (heightOf(self.root), node)

    def is_perfect_binary_tree(self) -> bool:
        height, total_nodes = self.heights_and_total_nodes()
        return ((1 << (height+1)) - 1) == total_nodes # 2^(h+1) - 1 == n
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool: # https://leetcode.com/problems/same-tree/description/
        if p == None and q == None:
            return True
        if p == None or q == None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) == True and self.isSameTree(p.right, q.right) == True
    
    def isSymmetric(self, root: TreeNode) -> bool: # https://leetcode.com/problems/symmetric-tree/
        def isSameTree(p: TreeNode, q: TreeNode) -> bool:
            if p == None and q == None:
                return True
            if p == None or q == None or p.val != q.val:
                return False
            return isSameTree(p.left, q.right) == True and isSameTree(p.right, q.left) == True
        
        return isSameTree(root.left, root.right)
    
    def maxDepth(self, root: TreeNode) -> int: # https://leetcode.com/problems/maximum-depth-of-binary-tree/
        q, level = deque([root] if root else []), 0

        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            level += 1
        
        return level
    
    def minDepth(self, root: TreeNode) -> int: # https://leetcode.com/problems/minimum-depth-of-binary-tree/
        q, level = deque([root] if root else []), 0

        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                if curNode.left == None and curNode.right == None:
                    return level + 1
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            level += 1
        
        return level # this return level only work when root == None
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool: # https://leetcode.com/problems/path-sum/description/
        if root == None: return False # Tree can be Empty, if Tree has min 1 node, don't need this if condition
        if root.left == None and root.right == None:
            return targetSum - root.val == 0
        return self.hasPathSum(root.left, targetSum - root.val) == True or self.hasPathSum(root.right, targetSum - root.val) == True
    
    def countNodes(self, root: TreeNode) -> int: # https://leetcode.com/problems/count-complete-tree-nodes/
        if root == None:
            return 0
        
        leftHeight = rightHeight = 0
        leftRoot = rightRoot = root

        while leftRoot:
            leftHeight += 1
            leftRoot = leftRoot.left
        while rightRoot:
            rightHeight += 1
            rightRoot = rightRoot.right
        
        if leftHeight == rightHeight:
            return (1 << leftHeight) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1 # 1 for the root node
        
    def binaryTreePaths(self, root: TreeNode) -> list[str]: # https://leetcode.com/problems/binary-tree-paths/description/
        # ans = []

        # def generateSubsets(Root: TreeNode, subset: list[int]) -> None:
        #     if Root == None: return
        #     subset.append(Root.val)
        #     if Root.left == None and Root.right == None: # then it's a leaf node
        #         ans.append('->'.join(map(str, subset)))
        #         subset.pop()
        #         return

        #     generateSubsets(Root.left, subset)
        #     generateSubsets(Root.right, subset)
        #     subset.pop()
        
        # generateSubsets(root, [])
        # return ans

        ans, q = [], deque([(root, f"{root.val}")])

        while q:
            for _ in range(len(q)):
                curNode, prevPath = q.popleft()
                if curNode.left == None and curNode.right == None:
                    ans.append(prevPath)
                    continue
                if curNode.left:
                    q.append((curNode.left,  f"{prevPath}->{curNode.left.val}"))
                if curNode.right:
                    q.append((curNode.right, f"{prevPath}->{curNode.right.val}"))

        return ans
    
    def invertTree(self, root: TreeNode) -> TreeNode: # https://leetcode.com/problems/invert-binary-tree/description/
        # if root == None:
        #     return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left) # ofc after the above swapping, root.left and right both changed
        # self.invertTree(root.right)
        # return root

        q = deque([root] if root else [])

        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                curNode.left, curNode.right = curNode.right, curNode.left
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
        
        return root
    
    def sumOfLeftLeaves(self, root: TreeNode, rootIsleftNode = False) -> int: # https://leetcode.com/problems/sum-of-left-leaves/
        # if root == None: return 0
        # if rootIsleftNode and root.left == None and root.right == None:
        #     return root.val
        # return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)

        q, leftLeaves = deque([root] if root else []), 0

        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                if curNode.left:
                    q.append(curNode.left)
                    if curNode.left.left == None and curNode.left.right == None: leftLeaves += curNode.left.val 
                if curNode.right:
                    q.append(curNode.right)
        
        return leftLeaves
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int: # https://leetcode.com/problems/diameter-of-binary-tree/
        diameter = 0

        def maxHeightOf(Root: TreeNode) -> int:
            nonlocal diameter
            if Root == None:
                return 0
            leftHeight  = maxHeightOf(Root.left)
            rightHeight = maxHeightOf(Root.right)

            diameter = max(diameter, leftHeight + rightHeight) # diameter = max(old_Diameter, new_Diameter)
            return max(leftHeight, rightHeight) + 1 # return max left/right height for the Root called this Root
        
        maxHeightOf(root)
        return diameter
    
    def findSecondMinimumValue(self, root: TreeNode) -> int: # https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
        def find2ndMinFrom(Root: TreeNode) -> int:
            if Root == None:
                return float('inf')
            curRootValue = Root.val if Root.val != root.val else float('inf')
            return min(curRootValue, find2ndMinFrom(Root.left), find2ndMinFrom(Root.right))
        
        secondMin = min(find2ndMinFrom(root.left), find2ndMinFrom(root.right))
        return secondMin if secondMin != float('inf') else -1
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool: # https://leetcode.com/problems/leaf-similar-trees/description/
        list1, list2 = [], []

        def addLeafsFrom(root: TreeNode, listNo: int) -> None:
            if root == None: return
            if root.left == None and root.right == None:
                if listNo == 1: list1.append(root.val)
                else:           list2.append(root.val)
            addLeafsFrom(root.left, listNo)
            addLeafsFrom(root.right, listNo)
        
        addLeafsFrom(root1, 1)
        addLeafsFrom(root2, 2)
        return list1 == list2
    
    def levelOrder(self, root: TreeNode) -> list[list[int]]: # https://leetcode.com/problems/binary-tree-level-order-traversal/description/
        ans = []

        def addAllFrom(Root: TreeNode, level: int) -> None:
            if Root == None: return
            if level > len(ans):
                ans.append([])
            ans[level-1].append(Root.val)
            addAllFrom(Root.left, level+1)
            addAllFrom(Root.right, level+1)
        
        addAllFrom(root, 1)
        return ans
    
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]: # https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
        q, ans = deque([root] if root else []), []

        while q:
            subList = []
            for _ in range(len(q)):
                curNode = q.popleft()
                subList.append(curNode.val)
                if curNode.left:  q.append(curNode.left)
                if curNode.right: q.append(curNode.right)
            ans.append(subList)
        
        for i in range(len(ans) >> 1):
            ans[i], ans[-(i+1)] = ans[-(i+1)], ans[i]
        return ans

    
def main():
    T = Tree()
    # for i in range(1, 8): T.insert(i)
    T.root = TreeNode(3)
    T.root.left = TreeNode(9)
    T.root.right = TreeNode(20)
    T.root.right.left = TreeNode(15)
    T.root.right.right = TreeNode(7)


    print(T.levelOrderBottom(T.root))
    

if __name__ == '__main__':
    main()