class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        new = ""

        for i in s:
            if i.upper() in s and i.lower() in s:
                if i.upper() > new:
                    new = i.upper()

        return new