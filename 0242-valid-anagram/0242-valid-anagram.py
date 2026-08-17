class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False
        
        d = {}
        d2 = {}

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1

        for i in t:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] = d2[i] + 1

        for key, value in d.items():
            if key not in d2 or value != d2[key]:
                return False

        return True