class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(str(n)) <= 3:
            return 0
        else:
            count = 0
        
            for i in range(1, n + 1):
            
                if i < 1000:
                    count += 0
            
                elif i < 1000000:
                    count += 1
            
                else:
                    count += 2
        return count