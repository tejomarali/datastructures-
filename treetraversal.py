"Construct a binary tree and perform various traversals."

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 
def inorderTraversal(root):
    answer = []
    inorderTraversalUtil(root, answer)
    return answer
def inorderTraversalUtil(root, answer):
    if root is None:
        return
    inorderTraversalUtil(root.left, answer)
    answer.append(root.val)
    inorderTraversalUtil(root.right, answer)
    return
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Inorder traversal is:-")
print(inorderTraversal(root))

def preorderTraversal(root):
    answer = []
    preorderTraversalUtil(root, answer)
    return answer
def preorderTraversalUtil(root, answer):
    if root is None:
        return 
    answer.append(root.val)
    preorderTraversalUtil(root.left, answer)
    preorderTraversalUtil(root.right, answer)
    return
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Preorder traversal is:-")
print(preorderTraversal(root))

def postorderTraversal(root):
    answer = []
    postorderTraversalUtil(root, answer)
    return answer
def postorderTraversalUtil(root, answer):
    if root is None:
        return
    postorderTraversalUtil(root.left, answer)
    postorderTraversalUtil(root.right, answer)
    answer.append(root.val)
    return
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Post order traversal is:-")
print(postorderTraversal(root))

CODE:-
Inorder traversal is:-
[4, 2, 5, 1, 3]
Preorder traversal is:-
[1, 2, 4, 5, 3]
Post order traversal is:-
[4, 5, 2, 3, 1]
