class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(n):
            if n%2==0:
                return True
            else:
                return False