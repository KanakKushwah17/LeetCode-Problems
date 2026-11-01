class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum=0
        if num <10 :
            return num
        while num>=10:
            sum=0
            while num>0:
                rem=num%10
                sum=rem+sum
                num=num//10
            num=sum
        return sum