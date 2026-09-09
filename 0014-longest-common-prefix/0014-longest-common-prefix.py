class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min=strs[0]
        for i in strs:
            if len(i)< len(min):
                min = i        
        
        res=""
        for i in range(len(min)):
            found=0
            for j in strs:
                found=0
                if min[:i+1]==j[:i+1]:
                    found=1
                else:
                    found=0
                    break
            if found==1:
                res=min[:i+1]
        return res
                