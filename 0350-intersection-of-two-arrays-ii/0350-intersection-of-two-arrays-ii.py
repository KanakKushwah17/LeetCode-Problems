class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
                :type nums2: List[int]
                :rtype: List[int]
                """
        nums1.sort()
        nums2.sort()
        
        
        new = []
        
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    new.append(i)
                    nums2.pop(j)
                    break
        
        return new