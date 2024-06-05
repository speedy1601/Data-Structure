from collections import deque

class TreeNode:
    def __init__(self, value, left = None, right = None, height = 0, balance_factor = 0):
        self.val = value
        self.left = left
        self.right = right
        self.height = height
        self.balance_factor = balance_factor  # in most code it isn't there.
    

class AVL_Tree:
    def __init__(self) -> None:
        self.root = None
    
    def get_height(self, node: TreeNode) -> int:
        return -1 if node == None else node.height
    
    def get_balanceFactor(self, node: TreeNode) -> int:
        return -1 if node == None else node.balance_factor
    
    def update_height_of(self, node: TreeNode):
        if node == None: return -1
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return node.height
    
    def update_balanceFactor_of(self, node: TreeNode):
        if node == None: return -1
        node.balance_factor = self.get_height(node.left) - self.get_height(node.right)
        return node.balance_factor
    
    def rotate_right(self, root: TreeNode) -> TreeNode:
        left = root.left
        rightOfLeft = left.right
        left.right = root
        root.left = rightOfLeft
        
        self.update_height_of(root)
        self.update_balanceFactor_of(root)
        self.update_height_of(left)
        self.update_balanceFactor_of(left)
        return left
    
    def rotate_left(self, root: TreeNode) -> TreeNode:
        right = root.right
        leftOfRight = right.left
        right.left = root
        root.right = leftOfRight
        
        self.update_height_of(root)
        self.update_balanceFactor_of(root)
        self.update_height_of(right)
        self.update_balanceFactor_of(right)
        return right

    def balance_curRoot_and_returnNewRoot(self, root: TreeNode) -> TreeNode:
        # step 1 : update the height of the current root
        self.update_height_of(root)

        # step 2 : update the Balance Factor of the current root
        bf = self.update_balanceFactor_of(root)

        # step 3 : rotate the current root if its Balance Factor is 2 or -2
        if bf == 2 or bf == -2:
            if bf == 2:  # LL / LR
                if root.left.balance_factor == 1:   # LL
                    return self.rotate_right(root)
                else: # LR
                    root.left = self.rotate_left(root.left)
                    return self.rotate_right(root)
                
            if bf == -2: # RR / RL
                if root.right.balance_factor == -1: # RR
                    return self.rotate_left(root)
                else: # RL
                    root.right = self.rotate_right(root.right)
                    return self.rotate_left(root)
        
        return root # if bf is not 2 or -2, then this line will execute denoting root doesn't need any rotation as its balanced already
    
    def insert_node(self,  root: TreeNode, key: int) -> TreeNode:
        # step 1 : Insert the Node in normal BST way
        if root == None:
            return TreeNode(key)
        
        if key < root.val:
            root.left  = self.insert_node(root.left,  key)
        else:
            root.right = self.insert_node(root.right, key)
                                                                            # After recursion stops going further, step 2 will run.
        # step 2 : Balance the Node / current root and return the new root to the caller function.
        return self.balance_curRoot_and_returnNewRoot(root)
        
    def already_inserted(self, root: TreeNode, key: int) -> bool:
        while root:
            if root.val == key:
                return True
            root = root.left if key < root.val else root.right
        return False
    
    def insert(self, value: int) -> None:
        if not self.already_inserted(self.root, value):
            self.root = self.insert_node(self.root, value)
    
    def successor_node_of(self, parentOfRoot: TreeNode, root: TreeNode) -> tuple[TreeNode]:
        while root.right:
            parentOfRoot = root
            root = root.right
        return (root, parentOfRoot) # (successor, parentOfSuccessor)

    def deleteNode_inBSTway(self, root: TreeNode, key: int, parentNode: TreeNode, parentValue: list[int]) -> TreeNode:
        if root == None:
            return None
        
        if root.val == key:
            if root.left and root.right:
                successor, parentOfSuccessor = self.successor_node_of(root, root.left)
                if successor.val < parentOfSuccessor.val: parentOfSuccessor.left  = successor.left
                else:                                     parentOfSuccessor.right = successor.left
                root.val = successor.val # finally replace the deleted_node's value with successor's value
                parentValue[0] = parentOfSuccessor.val                  # new line
                return root
            else:
                parentValue[0] = parentNode.val if parentNode else None # new line
                return root.left if root.left else root.right
        else:
            if key < root.val: root.left  = self.deleteNode_inBSTway(root.left,  key, root, parentValue)
            else:              root.right = self.deleteNode_inBSTway(root.right, key, root, parentValue)
            return root
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        parentValue = [None]  # parentValue is list here
        root = self.deleteNode_inBSTway(root, key, None, parentValue)
        parentValue = parentValue[0] # parentValue is int here
        if parentValue == None: return root

        def toFixTheBalance_traverse(curRoot: TreeNode):
            if curRoot.val == parentValue: # base case
                return self.balance_curRoot_and_returnNewRoot(curRoot)
            
            if parentValue < curRoot.val:
                curRoot.left  = toFixTheBalance_traverse(curRoot.left)
            else:
                curRoot.right = toFixTheBalance_traverse(curRoot.right)
            
            return self.balance_curRoot_and_returnNewRoot(curRoot)
        
        self.root =  toFixTheBalance_traverse(self.root)
        return self.root


    def printLevelByLevel(self, root = None) -> None:
        q = deque([root] if root else [self.root] if self.root else [])
        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                if curNode == None:
                    print('null', end=' ')
                    continue
                print(f"{curNode.val}({curNode.balance_factor})", end=' ')
                q.append(curNode.left)
                q.append(curNode.right)
            print()

def main():
    T = AVL_Tree()

    for i in range(1, 15):
        T.insert(i)
    
    T.printLevelByLevel()
    print()
    T.printLevelByLevel(T.deleteNode(T.root, 8))

if __name__ == '__main__':
    main()