class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(str(num))
        nums.sort()
        dig1 = nums[0]+ nums[3]
        dig2 = nums[1]+ nums[2]
        return int(dig1) + int(dig2)