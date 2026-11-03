class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        m=max(nums)
        for i in nums:
            count+=m-i
            
        return count