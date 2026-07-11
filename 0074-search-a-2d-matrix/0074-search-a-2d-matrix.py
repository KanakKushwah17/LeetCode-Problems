class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flag=0
        for sublist in matrix:
            for element in sublist:
                if element==target:
                    flag=1
        if flag==1:
            return True
        else:
            return False
                