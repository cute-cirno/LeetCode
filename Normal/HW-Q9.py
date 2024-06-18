class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtree_sum(node):
    if not node:
        return 0
    return node.val + subtree_sum(node.left) + subtree_sum(node.right)

def build_new_tree(node):
    if not node:
        return None
    left_sum = subtree_sum(node.left)
    right_sum = subtree_sum(node.right)
    new_node = TreeNode(left_sum + right_sum)
    new_node.left = build_new_tree(node.left)
    new_node.right = build_new_tree(node.right)
    return new_node

def print_tree(node, level=0, label='.'):
    if node:
        print(' ' * (level*4) + label + ':', node.val)
        print_tree(node.left, level+1, 'L')
        print_tree(node.right, level+1, 'R')

# 构建原始二叉树
root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.left.right = TreeNode(-2)
root.right.left = TreeNode(6)

# 构建新的二叉树
new_root = build_new_tree(root)

# 打印新的二叉树
print("新二叉树:")
print_tree(new_root)
