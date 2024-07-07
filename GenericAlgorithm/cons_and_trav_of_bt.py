class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def buildTreeFromPreIn(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_value = preorder.pop(0)
    root = TreeNode(root_value)
    inorder_index = inorder.index(root_value)

    root.left = buildTreeFromPreIn(preorder, inorder[:inorder_index])
    root.right = buildTreeFromPreIn(preorder, inorder[inorder_index+1:])

    return root


def buildTreeFromPostIn(postorder, inorder):
    if not postorder or not inorder:
        return None

    root_value = postorder.pop()
    root = TreeNode(root_value)
    inorder_index = inorder.index(root_value)

    root.right = buildTreeFromPostIn(postorder, inorder[inorder_index+1:])
    root.left = buildTreeFromPostIn(postorder, inorder[:inorder_index])

    return root

def preorderTraversal(root):
    if root is None:
        return []
    return [root.value] + preorderTraversal(root.left) + preorderTraversal(root.right)

def inorderTraversal(root):
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.value] + inorderTraversal(root.right)

def postorderTraversal(root):
    if root is None:
        return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.value]


# 示例输入
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

# 通过前序和中序重建二叉树
root_from_pre_in = buildTreeFromPreIn(preorder.copy(), inorder.copy())

# 通过后序和中序重建二叉树
root_from_post_in = buildTreeFromPostIn(postorder.copy(), inorder.copy())

# 前序遍历
print("前序遍历:", preorderTraversal(root_from_pre_in))

# 中序遍历
print("中序遍历:", inorderTraversal(root_from_pre_in))

# 后序遍历
print("后序遍历:", postorderTraversal(root_from_pre_in))
