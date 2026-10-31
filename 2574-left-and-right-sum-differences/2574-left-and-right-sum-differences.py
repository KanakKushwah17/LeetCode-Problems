class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return 0
        leftsum=[]
        rightsum=[]
        diff=[]
        sum=0
        
        for i in range(0,len(nums)):
            leftsum.append(sum)
            sum = sum+nums[i]
        
        sum=0
        for i in range(len(nums)-1,-1,-1):
            rightsum.append(sum)
            sum = nums[i] + sum
        rightsum.reverse()
        for i,j in zip(leftsum,rightsum):
            diff.append(abs(i-j))
        return diff
        