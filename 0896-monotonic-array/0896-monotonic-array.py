class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:

        n=sorted(nums)
        if nums==n or n[::-1]==nums:
            return True
        else:
            return False


                
            
            
