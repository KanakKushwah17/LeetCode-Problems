class Solution(object):
    def topKFrequent(self, nums, k):

        store = {}

        for i in nums:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1

        sorted_list = sorted(
            store.items(),
            key=lambda item: item[1],
            reverse=True
        )

        res = []

        for i in range(k):
            res.append(sorted_list[i][0])

        return res