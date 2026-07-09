class Solution(object):
    def findDifference(self, nums1, nums2):

        new1 = []

        for i in nums1:
            if i not in nums2:
                if i not in new1:
                    new1.append(i)

        new2 = []

        for i in nums2:
            if i not in nums1:
                if i not in new2:
                    new2.append(i)

        return [new1, new2]