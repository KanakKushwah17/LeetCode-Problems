class Solution(object):
    def isPalindrome(self, s):
        word = ''.join(c for c in s if c.isalnum()).lower()
        return word == word[::-1]


        