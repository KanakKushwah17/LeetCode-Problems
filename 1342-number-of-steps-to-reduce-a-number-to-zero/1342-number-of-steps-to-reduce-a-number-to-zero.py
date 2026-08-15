class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0

        while True:
            if num == 0:
                break
        
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
        
            count += 1
        
        return count