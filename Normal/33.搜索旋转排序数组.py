class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # 判断左侧是否有序
            if nums[left] <= nums[mid]:
                # 判断target是否在左侧
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 右侧必然有序
                # 判断target是否在右侧
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1

# 测试示例
sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))  # 输出: 4
print(sol.search([4,5,6,7,0,1,2], 3))  # 输出: -1
print(sol.search([1], 0))              # 输出: -1