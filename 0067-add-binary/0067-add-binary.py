class Solution(object):
    def addBinary(self, a, b):
       c=int(a,2)
       d=int(b,2)
       sum=c+d
       res=bin(sum)[2:]
       return res
        