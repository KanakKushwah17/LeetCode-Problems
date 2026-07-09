class Solution(object):
    def sortColors(self, nums):

        res = []

        for i in nums:
            if i == 0:
                res.append(i)

        for j in nums:
            if j == 1:
                res.append(j)

        for k in nums:
            if k == 2:
                res.append(k)

        for x in range(len(nums)):
            nums[x] = res[x]