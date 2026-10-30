class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        newword=set(word)
        print(newword)
        count=0
        
        for i in newword:
            if i.islower():
                if i.upper() in newword:
                    count=count+1
        return count