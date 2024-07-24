class Solution:
    def rob(self, root):
        if not root:
            return 0
        
        # 针对数组形式的完全二叉树使用辅助函数
        def rob_sub(i):
            if i >= len(root):
                return (0, 0)  # (不偷当前节点的最大金额, 偷当前节点的最大金额)
            
            if root[i] is None:
                return (0, 0)

            left = rob_sub(2 * i + 1)
            right = rob_sub(2 * i + 2)
            not_rob = max(left) + max(right)
            rob = root[i] + left[0] + right[0]

            return (not_rob, rob)
        
        result = rob_sub(0)
        return max(result)

# 示例输入
root1 = [3, 2, 3, None, 3, None, 1]
root2 = [3, 4, 5, 1, 3, None, 1]

sol = Solution()
print(sol.rob(root1))  # 输出应为 7
print(sol.rob(root2))  # 输出应为 9
