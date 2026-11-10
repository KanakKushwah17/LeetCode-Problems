class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=0
        pro=1
        num=n
        
        while n>0:
            rem=n%10
            s = s + rem
            pro = pro * rem
            n=n//10
            
        add=s+pro
        if num%add==0:
            return True
        else:
            return False