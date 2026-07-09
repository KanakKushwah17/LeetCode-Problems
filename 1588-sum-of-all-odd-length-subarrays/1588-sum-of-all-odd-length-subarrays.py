class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                sub=arr[i:j+1]
                if len(sub)%2!=0:
                    for k in sub:
                        sum+=k
        
        return sum