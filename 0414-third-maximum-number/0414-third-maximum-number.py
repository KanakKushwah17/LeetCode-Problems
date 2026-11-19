class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        result = sorted(set(nums), reverse=True)

        if len(result)<3:
            return result[0]
        else:
            return result[2]