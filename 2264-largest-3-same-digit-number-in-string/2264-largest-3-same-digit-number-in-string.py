class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_list =[]
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i+1]==num[i+2]:
                max_list.append(str(num[i]*3))
        if  max_list:
            return  max(max_list)
        return ""