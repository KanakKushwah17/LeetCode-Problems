class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag=-1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
                flag=0
        if flag==-1:
            return -1
        