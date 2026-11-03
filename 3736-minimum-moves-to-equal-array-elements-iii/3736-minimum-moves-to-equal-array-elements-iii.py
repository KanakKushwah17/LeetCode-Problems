class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        m=max(nums)
        for i in nums:
            while i<m:
                i=i+1
                count=count+1
            
        return count