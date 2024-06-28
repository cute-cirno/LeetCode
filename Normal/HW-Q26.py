class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    # 根节点是后序遍历的最后一个节点
    root_val = postorder.pop()
    root = TreeNode(root_val)

    # 在中序遍历中找到根节点的位置
    inorder_index = inorder.index(root_val)

    # 递归构建右子树和左子树
    root.right = buildTree(inorder[inorder_index + 1:], postorder)
    root.left = buildTree(inorder[:inorder_index], postorder)

    return root

def levelOrderTraversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current_level_size = len(queue)
        current_level_values = []

        for _ in range(current_level_size):
            node = queue.pop(0)
            current_level_values.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.extend(current_level_values)

    return result

# 输入处理
inorder = list(input().strip())
postorder = list(input().strip())

# 构建二叉树
root = buildTree(inorder, postorder)

# 层次遍历
result = levelOrderTraversal(root)

# 输出结果
print("".join(result))
