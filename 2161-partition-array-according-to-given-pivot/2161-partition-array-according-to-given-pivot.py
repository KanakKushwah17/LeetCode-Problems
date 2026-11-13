class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        dec=[]
        inc=[]
        new=[]
        p = 0
        for i in nums:
            if pivot < i:
                dec.append(i)
            elif pivot > i :
                inc.append(i)
            else:
                p+=1

        return inc+[pivot]*p+dec
