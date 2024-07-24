class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        i = 0
        max_jump = stones[1]-stones[0]
        while i+2 <= len(stones)-1:
            max_jump = max(max_jump, stones[i+2]-stones[i])
            i += 2
        if i > len(stones)-1:
            i = len(stones)-1
            max_jump = max(max_jump, stones[i]-stones[i-1])
        i = 1
        while i+2 <= len(stones)-1:
            max_jump = max(max_jump, stones[i+2]-stones[i])
            i += 2
        if i > len(stones)-1:
            i = len(stones)-1
            max_jump = max(max_jump, stones[i]-stones[i-1])
        return max_jump