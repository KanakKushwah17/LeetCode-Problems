class Solution(object):
    def searchMatrix(self, matrix, target):

        for sublist in matrix:
            for element in sublist:

                if element == target:
                    return True

        return False