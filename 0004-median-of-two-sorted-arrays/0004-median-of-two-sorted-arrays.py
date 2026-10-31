class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        merge = sorted(nums1 + nums2)

        n = len(merge)
        mid = n // 2

        if n % 2 == 0:
            return (merge[mid-1] + merge[mid]) / 2.0

        else:
            return merge[mid]