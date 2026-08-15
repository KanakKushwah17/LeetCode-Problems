class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        sum=0
        for i in nums:
            sum=sum+i
            new.append(sum)
        return new 
        