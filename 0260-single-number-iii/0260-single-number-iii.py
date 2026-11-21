class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        new=[]
        for i in nums:
            if nums.count(i) == 1:
                new.append(i)
        return new
