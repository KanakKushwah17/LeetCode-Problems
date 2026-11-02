class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel=""
        index=[]
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                vowel=vowel+s[i]
                index.append(i)
                
        new=vowel[::-1]
        s=list(s)
        for i in range(len(index)):
            s[index[i]] = new[i]
            
        return "".join(s)
        
        