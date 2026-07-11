class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min=nums[0]
        for i in range(len(nums)):
            if min>nums[i]:
                min=nums[i]
        return min
                