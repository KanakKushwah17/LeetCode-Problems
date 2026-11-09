class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new=[]   
        s=sorted(nums)
        for i in range(len(s)):
            if s[i] == target:
                new.append(i)
        return new
        