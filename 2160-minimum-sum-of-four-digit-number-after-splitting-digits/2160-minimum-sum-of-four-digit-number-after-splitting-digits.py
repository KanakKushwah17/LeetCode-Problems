class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(str(num))
        nums.sort()
        dig1 = nums[0]+ nums[2]
        dig2 = nums[1]+ nums[3]
        return int(dig1) + int(dig2)