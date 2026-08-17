class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new=""
        for i in s:
            if i.isalnum():
                new=new+i.lower()
        print(new)
        if new==new[::-1]:
            return True
        else:
            return False


        