class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans = []

        for x in nums:
            count = 0

            for y in nums:
                if y < x:
                    count += 1

            ans.append(count)

        return ans