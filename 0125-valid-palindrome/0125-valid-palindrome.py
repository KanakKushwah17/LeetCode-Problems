class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
                """
        new=""
        news=""
        for i in s:
            for j in i:
                if "a" <= j <= "z" or  "A" <= j <= "Z" or "0" <= i <= "9":
                    news=j.lower()+news
        print(news)
        for i in news:
            for j in i:
                new=j+new
        if new==news:
            return True
        else:
            return False
