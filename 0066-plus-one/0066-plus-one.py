class Solution(object):
    def plusOne(self, digits):

        s1 = ""

        for i in digits:
            s1 += str(i)

        s2 = int(s1) + 1

        ans = []
        for i in str(s2):
            ans.append(int(i))

        return ans