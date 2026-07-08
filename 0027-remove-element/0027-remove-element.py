class Solution(object):
    def removeElement(self, nums, val):
        new = []

        for i in nums:
            if i != val:
                new.append(i)

        for i in range(len(new)):
            nums[i] = new[i]

        return len(new)