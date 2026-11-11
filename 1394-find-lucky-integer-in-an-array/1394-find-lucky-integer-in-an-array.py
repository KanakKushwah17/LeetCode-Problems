class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        arr1={}
        for i in arr:
            if i not in arr1:
                arr1[i]=1
            else:
                arr1[i]=arr1[i]+1
        largest=-1
        for key,value in arr1.items():
            if key==value:
                largest=max(largest,key)
        return largest
        