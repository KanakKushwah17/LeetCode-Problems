class Solution(object):
    def searchRange(self, nums, target):

        new = []

        for i in range(len(nums)):
            if nums[i] == target:
                new.append(i)

        if len(new) == 0:
            return [-1, -1]

        return [new[0], new[-1]]