from collections import deque
import time
class TreeNode:
    def __init__(self, value):
        self.data = value
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
                print(curNode.data, end=' ')
                if curNode.left:  q.append(curNode.left)
                if curNode.right: q.append(curNode.right)
            print()
    
    def print_preOrder(self, root) -> None:
        if root == None:
            return
        print(root.data, end=' ')
        self.print_preOrder(root.left)
        self.print_preOrder(root.right)
    
    def preorderTraversal(self, root: TreeNode) -> list[int]: # https://leetcode.com/problems/binary-tree-preorder-traversal/
        stack, preorderList = [], []
        curNode = root

        while curNode or stack:
            while curNode:
                stack.append(curNode)
                preorderList.append(curNode.data)
                curNode = curNode.left
            curNode = stack.pop().right
        
        return preorderList

        # stack, preorderList = [root] if root else [], []

        # while stack:
        #     curNode = stack.pop()
        #     preorderList.append(curNode.data)
        #     if curNode.right:
        #         stack.append(curNode.right)
        #     if curNode.left:
        #         stack.append(curNode.left)
        
        # return preorderList

    def print_inOrder(self, root) -> None:
        if root == None:
            return
        self.print_inOrder(root.left)
        print(root.data, end=' ')
        self.print_inOrder(root.right)
    
    def inorderTraversal(self, root: TreeNode) -> list[int]: # https://leetcode.com/problems/binary-tree-inorder-traversal/description/
        stack, inorderList = [], []
        curNode = root

        while curNode or stack:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            curNode = stack.pop()
            inorderList.append(curNode.data)
            curNode = curNode.right
        
        return inorderList
    
    def print_postOrder(self, root) -> None:
        if root == None:
            return
        self.print_postOrder(root.left)
        self.print_postOrder(root.right)
        print(root.data, end=' ')

    def postorderTraversal(self, root: TreeNode) -> list[int]: # https://leetcode.com/problems/binary-tree-postorder-traversal/description/
        stack, postOrderList, visited = [], [], {None}
        curNode = root

        while curNode or stack:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            
            curNode = stack[-1]
            while curNode and (curNode.left in visited and curNode.right in visited):
                postOrderList.append(stack.pop().data) # stack.pop() == curNode
                visited.add(curNode)
                curNode = stack[-1] if stack else None
            curNode = stack[-1].right if stack else None
           
        return postOrderList
    
    def tree_max(self) -> int:
        def max_value_of(root) -> int: # similar to preOrder traversal where root process first, then root.left and root.right
            if root == None:
                return float('-inf')
            return max(root.data, max_value_of(root.left), max_value_of(root.right))
        return max_value_of(self.root)
    
    def tree_height(self) -> int: # distance from the Farthest Node to Root Node e.g. 4 -> 3, Distance from 3 to 4 is 1
        def heightOf(root) -> int:
            if root == None:
                return -1
            return max(1 + heightOf(root.left), 1 + heightOf(root.right))
        return heightOf(self.root)
    
    def total_nodes(self) -> int:
        def total_nodes_from(root) -> int:
            if root == None:
                return 0
            return 1 + total_nodes_from(root.left) + total_nodes_from(root.right)
        return total_nodes_from(self.root)
    
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
            return any((root.data == value, search_from(root.left), search_from(root.right)))
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
    
def main():
    T = Tree()
    for i in range(1, 8):
        T.insert(i)
    T.root.left.left = None
    # T.queue[0].right = TreeNode(16)
    # T.queue[-1].right = TreeNode(17)
    # T.print_preOrder(T.root);  print()
    # T.print_inOrder(T.root);   print()
    # T.print_postOrder(T.root); print()
    # print(T.tree_max())
    # print(T.tree_height())
    # print(T.total_nodes())
    # print(T.total_leaf_nodes())
    # print(T.is_exist(19))
    # print(T.is_perfect_binary_tree())
    # print(T.inorderTraversal(T.root))
    T.print_postOrder(T.root); print()
    print(T.postorderTraversal(T.root))

if __name__ == '__main__':
    main()