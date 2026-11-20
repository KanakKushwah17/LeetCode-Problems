class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total = sum(int(i) for i in str(x))

        if x % total == 0:
            return total
        else:
            return -1